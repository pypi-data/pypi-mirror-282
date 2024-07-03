import json
import os

import click

from morph.cli.flags import Flags
from morph.task.base import BaseTask
from morph.task.utils.morph import MorphYaml
from morph.task.utils.sqlite import SqliteDBManager


class PrintResourceTask(BaseTask):
    def __init__(self, args: Flags):
        super().__init__(args)
        self.args = args

        self.alias = args.ALIAS
        self.path = args.PATH

        # Initialize MorphYaml
        try:
            self.project_root = MorphYaml.find_abs_project_root_dir()
        except FileNotFoundError as e:
            click.echo(click.style(str(e), fg="red"))
            raise e
        self.morph_config = MorphYaml.init(self.project_root)

        # Initialize SQLite database
        self.db_manager = SqliteDBManager(
            self.project_root, os.path.join(self.project_root, "morph_project.sqlite3")
        )
        self.db_manager.initialize_database()

    def run(self):
        if self.alias:
            resource = self.morph_config.find_resource_by_alias(
                self.alias, self.db_manager
            )
            if resource:
                resource_full_path = self._convert_to_full_paths(resource)
                click.echo(json.dumps(resource_full_path, indent=2))
            else:
                click.echo(f"Alias {self.alias} not found.")
        elif self.path:
            resource = self.morph_config.find_resource_by_path(
                self.path, self.project_root, self.db_manager
            )
            if resource:
                resource_full_path = self._convert_to_full_paths(resource)
                click.echo(json.dumps(resource_full_path, indent=2))
            else:
                click.echo(f"Path {self.path} not found.")
        else:
            click.echo("Either --alias or --path must be provided.")

    def _convert_to_full_paths(self, resource: dict) -> dict:
        full_path_resource = {}
        for key, value in resource.items():
            if key == "path" or key == "output_path":
                full_path_resource[key] = os.path.abspath(
                    os.path.join(self.project_root, value)
                )
            else:
                full_path_resource[key] = value
        return full_path_resource
