import os
from collections import defaultdict, deque
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

import click
import yaml

from morph.task.constant.project_config import ProjectConfig
from morph.task.utils.sqlite import SqliteDBManager


class CellType(str, Enum):
    SQL = "sql"
    PYTHON = "python"
    MARKDOWN = "markdown"
    FILE = "file"
    DIRECTORY = "directory"


@dataclass
class CellCoordinates:
    x: int
    y: int
    w: int
    h: int


@dataclass
class MorphCell:
    alias: str
    cellType: CellType
    coordinates: CellCoordinates
    parents: List[str] = field(default_factory=list)


@dataclass
class MorphYaml:
    version: str
    resources: Dict[str, Dict[str, str]]
    canvases: Dict[str, Dict[str, Any]]

    @staticmethod
    def init(project_root_path: str) -> "MorphYaml":
        morph_yaml_path = os.path.join(project_root_path, ProjectConfig.MORPH_YAML)
        if not os.path.isfile(morph_yaml_path):
            raise FileNotFoundError(f"morph.yaml not found in {project_root_path}")

        with open(morph_yaml_path, "r") as file:
            data = yaml.safe_load(file)

        return MorphYaml.from_dict(data)

    def to_dict(self):
        updated_canvases = {}
        for canvas, cells_dict in self.canvases.items():
            if "cells" not in cells_dict:
                updated_canvases[canvas] = {"cells": cells_dict}
            else:
                updated_canvases[canvas] = cells_dict
        return {
            "version": self.version,
            "resources": self.resources,
            "canvases": updated_canvases,
        }

    @staticmethod
    def from_dict(data: dict):
        resources = data.get("resources", {})
        canvases = {
            canvas: cells.get("cells", cells)
            for canvas, cells in data.get("canvases", {}).items()
        }
        return MorphYaml(
            version=data["version"], resources=resources, canvases=canvases
        )

    @staticmethod
    def find_abs_project_root_dir(start_dir: Optional[str] = os.getcwd()) -> str:
        current_dir = start_dir
        while current_dir != os.path.dirname(current_dir):
            morph_yaml_path = os.path.join(current_dir, ProjectConfig.MORPH_YAML)
            if os.path.isfile(morph_yaml_path):
                return os.path.abspath(os.path.dirname(morph_yaml_path))
            current_dir = os.path.dirname(current_dir)
        raise FileNotFoundError(
            f"{ProjectConfig.MORPH_YAML} not found in the current directory or any parent directories."
        )

    def find_or_create_alias(
        self, filename: str, project_root: str, db_manager: SqliteDBManager
    ) -> str:
        normalized_path = db_manager.normalize_path(filename, project_root)

        # First, search in the SQLite database
        resource = db_manager.get_resource_by_path(normalized_path)
        if resource:
            return resource["alias"]

        # If not found, search in the YAML file
        for alias, resource in self.resources.items():
            resource_path = db_manager.normalize_path(resource["path"], project_root)
            if resource_path == normalized_path:
                # Sync to SQLite
                db_manager.replace_resource_record(alias, normalized_path, resource)
                return alias

        # Generate new alias if the resource is not defined yet in the morph.yaml
        base_name = os.path.splitext(os.path.basename(filename))[0]
        new_alias = base_name
        alias_count = defaultdict(int)

        for alias in self.resources.keys():
            if alias.startswith(base_name):
                alias_count[alias] += 1

        if new_alias in self.resources:
            new_alias = f"{base_name}_{alias_count[base_name]}"

        while new_alias in self.resources:
            alias_count[base_name] += 1
            new_alias = f"{base_name}_{alias_count[base_name]}"

        self.resources[new_alias] = {"path": filename}

        # Sync new resource to SQLite
        db_manager.replace_resource_record(
            new_alias, filename, self.resources[new_alias]
        )

        click.echo(
            click.style(f"Resource {filename} added with alias {new_alias}", fg="green")
        )

        return new_alias

    def find_resource_by_path(
        self, path: str, project_root: str, db_manager: SqliteDBManager
    ) -> Optional[Dict[str, Any]]:
        normalized_path = db_manager.normalize_path(path, project_root)

        # First, search in the SQLite database
        resource = db_manager.get_resource_by_path(normalized_path)
        if resource:
            return resource

        # If not found, search in the YAML file and sync to SQLite
        for alias, resource in self.resources.items():
            resource_path = db_manager.normalize_path(resource["path"], project_root)
            if resource_path == normalized_path:
                db_manager.replace_resource_record(alias, normalized_path, resource)
                return resource

        return None

    def find_resource_by_alias(
        self, alias: str, db_manager: SqliteDBManager
    ) -> Optional[Dict[str, Any]]:
        # First, search in the SQLite database
        resource = db_manager.get_resource_by_alias(alias)
        if resource:
            return resource

        # If not found, search in the YAML file and sync to SQLite
        resource = self.resources.get(alias)
        if resource:
            db_manager.replace_resource_record(alias, resource["path"], resource)
            return resource

        return None

    def get_dag_execution_order(self, canvas_name: str, start_alias: str) -> List[str]:
        dag = {}
        visited = set()
        queue = deque([start_alias])

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            cell = self.canvases[canvas_name].get(current)
            if cell:
                parents = cell.get("parents", [])
                dag[current] = parents
                for parent in parents:
                    if parent not in visited:
                        queue.append(parent)

        execution_order = []
        executed = set()
        for node in dag:
            self._collect_execution_order(node, executed, dag, execution_order)

        return execution_order

    def _collect_execution_order(self, node, executed, dag, execution_order):
        if node in executed:
            return

        for parent in dag.get(node, []):
            self._collect_execution_order(parent, executed, dag, execution_order)

        execution_order.append(node)
        executed.add(node)
