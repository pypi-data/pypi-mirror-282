import json
import os
import sqlite3
from datetime import datetime

import yaml

from morph.task.constant.project_config import ProjectConfig


class SqliteDBManager:
    def __init__(self, project_root: str, db_path: str):
        self.project_root = project_root
        self.db_path = db_path

    def initialize_database(self):
        # Connect to the SQLite database
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # Create "runs" table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS runs (
                run_id TEXT,
                canvas TEXT,
                cell_alias TEXT,
                is_dag BOOLEAN,
                status TEXT,
                error TEXT,
                started_at TEXT,
                ended_at TEXT,
                log TEXT,
                result TEXT,
                PRIMARY KEY (run_id, canvas, cell_alias)
            )
            """
        )

        # Create "resources" table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS resources (
                alias TEXT PRIMARY KEY,
                path TEXT,
                attributes TEXT
            )
            """
        )

        # Create indexes for "runs" table
        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_runs_cell_alias ON runs(cell_alias)
            """
        )

        # Create indexes for "resources" table
        cursor.execute(
            """
            CREATE INDEX IF NOT EXISTS idx_resources_path ON resources(path)
            """
        )

        # Commit changes and close the connection
        conn.commit()
        conn.close()

    def insert_run_record(
        self, run_id, canvas, cell_alias, is_dag, status, started_at, log_path
    ):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("BEGIN TRANSACTION")
            cursor.execute(
                """
                INSERT INTO runs (run_id, canvas, cell_alias, is_dag, status, started_at, ended_at, log, result)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    run_id,
                    canvas,
                    cell_alias,
                    is_dag,
                    status,
                    started_at,
                    None,
                    log_path,
                    None,
                ),
            )
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def update_run_record(
        self, run_id, canvas, cell_alias, new_status, error=None, output_file=None
    ):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        ended_at = datetime.now().isoformat()

        try:
            cursor.execute("BEGIN TRANSACTION")
            if canvas is None:
                cursor.execute(
                    """
                    UPDATE runs
                    SET status = ?, error = ?, ended_at = ?, result = ?
                    WHERE run_id = ? AND cell_alias = ?
                    """,
                    (new_status, error, ended_at, output_file, run_id, cell_alias),
                )
            else:
                cursor.execute(
                    """
                    UPDATE runs
                    SET status = ?, error = ?, ended_at = ?, result = ?
                    WHERE run_id = ? AND canvas = ? AND cell_alias = ?
                    """,
                    (
                        new_status,
                        error,
                        ended_at,
                        output_file,
                        run_id,
                        canvas,
                        cell_alias,
                    ),
                )
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def sync_resources_from_yaml(self):
        morph_yaml_path = os.path.join(self.project_root, ProjectConfig.MORPH_YAML)
        if not os.path.isfile(morph_yaml_path):
            raise FileNotFoundError(f"morph.yaml not found in {self.project_root}")

        with open(morph_yaml_path, "r") as file:
            morph_config = yaml.safe_load(file)

        resources = morph_config.get("resources", {})

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("BEGIN TRANSACTION")
            cursor.execute("DELETE FROM resources")

            for alias, resource in resources.items():
                attributes = json.dumps(resource)
                cursor.execute(
                    """
                    INSERT INTO resources (alias, path, attributes)
                    VALUES (?, ?, ?)
                    """,
                    (
                        alias,
                        resource.get("path"),
                        attributes,
                    ),
                )
            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def get_resource_by_alias(self, alias):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT alias, path, attributes FROM resources WHERE alias = ?", (alias,)
        )
        resource = cursor.fetchone()

        conn.close()

        if resource:
            attributes = json.loads(resource[2])
            return {
                "alias": resource[0],
                "path": resource[1],
                **attributes,
            }
        return None

    def get_resource_by_path(self, path):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT alias, path, attributes FROM resources WHERE path = ?", (path,)
        )
        resource = cursor.fetchone()

        conn.close()

        if resource:
            attributes = json.loads(resource[2])
            return {
                "alias": resource[0],
                "path": resource[1],
                **attributes,
            }
        return None

    def replace_resource_record(self, alias, path, attributes):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        try:
            cursor.execute("BEGIN TRANSACTION")

            # Check if the record exists
            cursor.execute(
                """
                SELECT 1 FROM resources WHERE alias = ?
                """,
                (alias,),
            )
            exists = cursor.fetchone()

            # If the record exists, delete it
            if exists:
                cursor.execute(
                    """
                    DELETE FROM resources WHERE alias = ?
                    """,
                    (alias,),
                )

            # Insert new record
            cursor.execute(
                """
                INSERT INTO resources (alias, path, attributes)
                VALUES (?, ?, ?)
                """,
                (
                    alias,
                    path,
                    json.dumps(attributes),
                ),
            )

            conn.commit()
        except sqlite3.Error as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    @staticmethod
    def normalize_path(filename: str, project_root: str) -> str:
        return os.path.abspath(os.path.normpath(os.path.join(project_root, filename)))
