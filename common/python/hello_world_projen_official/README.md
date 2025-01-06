# projen_world

Python project created using official Projen constructs to evaluate how good it is.

Initial creation based on https://projen.io/docs/quick-starts/python/hello-world/

`npx projen new python --name=projen_world`

## Spike impression

The official constructs for Python (PythonProject) lack:
  - RUFF/linting/audit/formatter
  - Test coverage configuration
  - pyproject.toml with pip
  - PythonProject cannot be used in Python flavor with all its methods (couldn't understand why)
