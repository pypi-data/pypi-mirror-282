import os

import click
import toml
import yaml

from morph.cli.flags import Flags
from morph.task.base import BaseTask
from morph.task.constant.project_config import ProjectConfig
from morph.task.utils.morph import MorphYaml
from morph.task.utils.sqlite import SqliteDBManager


class NewTask(BaseTask):
    def __init__(self, args: Flags, project_directory):
        super().__init__(args)
        self.args = args
        self.project_directory = project_directory

    def run(self):
        click.echo("Creating new Morph project...")

        # Create the project structure
        if not os.path.exists(self.project_directory):
            os.makedirs(self.project_directory, exist_ok=True)
        config_file = os.path.join(self.project_directory, ProjectConfig.MORPH_YAML)
        if os.path.exists(config_file):
            click.echo(
                f"The directory is already a Morph project: {self.project_directory}"
            )
            return False
        else:
            self._create_project_structure()

        # Initialize the project database
        db_path = os.path.join(self.project_directory, "morph_project.sqlite3")
        db_manager = SqliteDBManager(self.project_directory, db_path)
        db_manager.initialize_database()

        click.echo("Project setup completed successfully.")
        self._display_post_setup_message()
        return True

    def _create_project_structure(self):
        directories = [
            ##########################################
            # File
            ##########################################
            f"{self.project_directory}/src/files/python",
            f"{self.project_directory}/src/files/sql",
            ##########################################
            # Data
            ##########################################
            f"{self.project_directory}/src/{ProjectConfig.OUTPUTS_DIR}",
            ##########################################
            # Lib
            ##########################################
            f"{self.project_directory}/src/lib/sql",
            f"{self.project_directory}/src/lib/python",
            ##########################################
            # Knowledge
            ##########################################
            f"{self.project_directory}/knowledge",
        ]

        files = {
            ##########################################
            # Canvas
            ##########################################
            f"{self.project_directory}/src/files/README.md": self._generate_canvas_readme(),
            f"{self.project_directory}/src/files/python/example_python_cell.py": self._generate_example_python_cell(),
            f"{self.project_directory}/src/files/sql/example_sql_cell.sql": self._generate_example_sql_cell(),
            ##########################################
            # Lib
            ##########################################
            f"{self.project_directory}/src/lib/README.md": self._generate_lib_readme(),
            ##########################################
            # Knowledge
            ##########################################
            f"{self.project_directory}/knowledge/README.md": self._generate_knowledge_readme(),
            ##########################################
            # Project Root
            ##########################################
            f"{self.project_directory}/morph_project.sqlite3": "",
            f"{self.project_directory}/.env": self._generate_project_dotenv_content(),
            f"{self.project_directory}/.gitignore": self._generate_project_gitignore_content(),
            f"{self.project_directory}/pyproject.toml": self._generate_project_toml_content(),
            f"{self.project_directory}/{ProjectConfig.MORPH_YAML}": self._generate_morph_config_content(),
        }

        # Create directories
        for directory in directories:
            os.makedirs(directory, exist_ok=True)

        # Create files with default content
        for filepath, content in files.items():
            with open(filepath, "w") as f:
                f.write(content)

    def _display_post_setup_message(self):
        message = (
            f"\nTo activate the project environment and install dependencies, "
            f"run the following commands:\n\n"
            f"    cd {os.path.abspath(self.project_directory)}\n"
            f"    poetry install\n\n"
            f"If you don't have Poetry installed, visit https://python-poetry.org/docs/#installation "
            f"for installation instructions.\n"
        )
        click.echo(click.style(message, fg="yellow"))

    @staticmethod
    def _generate_canvas_readme():
        return """# Canvas

This directory contains various canvases used in the project. Each canvas may consist of multiple visualization or data transformation scripts.

## Canvas 1

Description of what Canvas 1 does and its purpose in the project."""

    @staticmethod
    def _generate_lib_readme():
        return """# Library Modules

This directory contains custom libraries or scripts that can be reused across different parts of the project.

## SQL Library

Contains reusable SQL queries or scripts.

## Python Library

Contains Python utility functions and classes."""

    @staticmethod
    def _generate_knowledge_readme():
        return """# Knowledge Base

This directory is intended to store documentation, notes, or informative Markdown files that provide insights or useful information about the project."""

    @staticmethod
    def _generate_example_python_cell():
        return """\
import pandas as pd

from typing import Dict
from datetime import datetime
from morphdb_utils.api import execute_sql, load_data, ref
from morphdb_utils.annotations import transform

# The `data` variable prepares the data for processing in the main functions.
# For more information, please read the documentation at https://docs.morphdb.io/dbutils
data = {}

# The main function runs on the cloud when you click "Run".
# It's used by the data pipeline on the canvas to execute your Directed Acyclic Graph (DAG).
@transform
def main(data: Dict[str, pd.DataFrame]):
    # This is where you write your code.
    example = {
        "Name": ["John Doe", "Jane Smith", "Emily Zhang"],
        "Age": [28, 34, 22],
        "Occupation": ["Software Engineer", "Data Scientist", "Marketing Manager"]
    }
    return pd.DataFrame(example)
"""

    @staticmethod
    def _generate_example_sql_cell():
        return "select 1 as test;"

    @staticmethod
    def _generate_project_dotenv_content():
        dotenv_content = """# Environment Configuration File
# This file contains environment variables that configure the application.
# Each line in this file must be in VAR=VAL format.

# Set the TZ variable to the desired timezone.
# In Morph cloud platform, the change will take effect after the next run.
TZ=Asia/Tokyo"""
        return dotenv_content

    @staticmethod
    def _generate_project_toml_content():
        config = {
            "tool": {
                "poetry": {
                    "name": "morph",
                    "version": "0.1.0",
                    "description": "Auto-generated Morph project.",
                    "authors": [],
                    "dependencies": {
                        "python": "^3.9",
                        "pandas": "2.1.3",
                        "requests": "2.31.0",
                        "xlrd": "2.0.1",
                        "matplotlib": "3.5.2",
                        "boto3": "^1.26.80",
                        "pypika": "^0.48.9",
                        "pydantic": "^2.5.3",
                        "sqlparse": "^0.4.4",
                        "line-profiler": "^4.1.2",
                        "urllib3": "1.26.18",
                        "plotly": "^5.18.0",
                        "kaleido": "0.2.1",
                        "openpyxl": "^3.1.2",
                        "seaborn": "^0.13.2",
                        "aws-lambda-powertools": "^2.34.2",
                        "simplejson": "^3.19.2",
                        "pyppeteer": "^2.0.0",
                    },
                    "group": {
                        "dev": {
                            "dependencies": {
                                "python-dotenv": "^1.0.0",
                                "types-requests": "^2.28.11.13",
                                "pytest": "^7.4.4",
                                "black": "^24.1.0",
                                "flake8": "^5.0.4",
                                "mypy": "^1.8.0",
                                "pre-commit": "^3.6.0",
                                "types-pytz": "^2023.3.1.1",
                                "pytest-asyncio": "^0.23.3",
                            }
                        }
                    },
                }
            },
            "build-system": {
                "requires": ["poetry-core>=1.0.0"],
                "build-backend": "poetry.core.masonry.api",
            },
        }
        return toml.dumps(config)

    @staticmethod
    def _generate_morph_config_content():
        morph_yaml = MorphYaml(
            version="0.1",
            resources={
                "example_python_cell": {
                    "path": "./src/files/python/example_python_cell.py",
                    "output_path": "./src/data/outputs/output_example_python_cell/example_python_cell.csv",
                },
                "example_sql_cell": {"path": "./src/files/sql/example_sql_cell.sql"},
            },
            canvases={
                "canvas1": {
                    "cells": {
                        "example_python_cell": {
                            "coordinates": {"x": 0, "y": 0, "w": 600, "h": 400},
                            "parents": [],
                        },
                        "example_sql_cell": {
                            "coordinates": {"x": 0, "y": 450, "w": 600, "h": 400},
                            "parents": [],
                        },
                    }
                }
            },
        )
        return yaml.dump(morph_yaml.to_dict(), sort_keys=False)

    @staticmethod
    def _generate_project_gitignore_content():
        return """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# PEP 582; used by e.g. pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.env.local
.venv
venv/
ENV/
env/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
.idea/

# VSCode
.vscode/

# Poetry
.poetry-cache

# pytest
.pytest_cache/

# MacOS system files
.DS_Store

# Windows thumbnail cache
Thumbs.db

# Logs
*.log
*.out"""
