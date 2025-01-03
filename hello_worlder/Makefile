PYTHON_VENV_PATH = $(PWD)/.venv

# build module
build: venv-prepare
	@echo "Installing dependencies..."
	$(PYTHON_VENV_PATH)/bin/pip3 install --require-virtualenv -c constraints.txt .[dev]
	@rm -rf build

test:
	$(PYTHON_VENV_PATH)/bin/pytest --cov=src

lint:
	@echo "\n>>> Code type checks (mypy)..."
	$(PYTHON_VENV_PATH)/bin/mypy src tests

	@echo "\n>>> Code format checks (RUFF)..."
	$(PYTHON_VENV_PATH)/bin/ruff format --check src tests

	@echo "\n>>> Code lint checks (RUFF)..."
	$(PYTHON_VENV_PATH)/bin/ruff check src tests

	@echo "\n>>> Dependency vulnerability checks (pip-audit)..."
	$(PYTHON_VENV_PATH)/bin/pip-audit --cache-dir .cache/.audit_cache

lint-fix:
	$(PYTHON_VENV_PATH)/bin/ruff format
	$(PYTHON_VENV_PATH)/bin/ruff check --fix

update-lockfile:
	@echo "Updating lock file (constraints.txt)..."
	$(PYTHON_VENV_PATH)/bin/pip-compile --all-build-deps --all-extras --strip-extras \
		--output-file=constraints.txt pyproject.toml
	make build

all: build test lint

# run jupyer locally
start:
	$(PYTHON_VENV_PATH)/bin/jupyter lab --port 8888 --NotebookApp.iopub_data_rate_limit=1.0e10

clean:
	rm -rf $(PYTHON_VENV_PATH)
	rm -rf build .cache .coverage

# install required tools
prepare:
	brew install python3

# python virtual environment management
venv-prepare:
	@echo Preparing Python venv at $(PYTHON_VENV_PATH)...
	python3 -m venv $(PYTHON_VENV_PATH)

venv-activate:
	@echo "run 'source .venv/bin/activate' manually"
