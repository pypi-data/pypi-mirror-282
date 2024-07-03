# Morph

## How to Contribute

### Setting up the development environment

This project uses [pre-commit](https://pre-commit.com/) to enforce code quality and consistency. To install the pre-commit hooks, run the following command:

```shell
pre-commit install
```

### Run poetry install

```shell
poetry cache clear --all pypi

poetry update

poetry install --all-extras
```

### Contributing code

You can install your CLI tool locally to test it:

```shell
pip install --editable .
```

This command installs the package in editable mode, which means changes to the source files will immediately affect the installed package without needing a reinstallation.

## Available commands

### init

Initialize a new Morph project.

Example:
```shell
morph init
```

### new

Create a new Morph project directory.

Example:
```shell
morph new ~/Downloads/test
```

### run

Run an SQL or Python file and produce the results in the output file.

Example:
```shell
# Run a Python file
morph run ~/Downloads/test/src/canvas/canvas1/example_python_cell.py

# Run an SQL file
morph run ~/Downloads/test/src/canvas/canvas1/example_sql_cell.sql
```

### create-file

Create a new file with the specified settings.

Example:
```shell
morph create-file ~/Downloads/test/src/canvas/canvas1/hello.py '{"x": 0, "y": 0, "w": 0, "h": 0}' "print('Hello, World!')" transform '[]' English
```

### update-file

Update the content of an existing file.

Example:
```shell
morph update-file ~/Downloads/test/src/canvas/canvas1/hello.py "print('Updated content')"
```

### delete-file

Delete a specified file.

Example:
```shell
morph delete-file ~/Downloads/test/src/canvas/canvas1/hello.py
```
