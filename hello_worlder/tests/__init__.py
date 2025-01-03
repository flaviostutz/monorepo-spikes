import sys
from pathlib import Path

# make tests load modules from workspace instead of the venv so we don't need
# to re-build everytime and also coverage works correctly too
sys.path.insert(0, f"{Path.cwd()}/src")
