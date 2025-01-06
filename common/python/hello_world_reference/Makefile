VENV_PATH = .venv

# build module
build: prepare-venv
	@echo "Installing dependencies..."
	$(VENV_PATH)/bin/pip3 install --require-virtualenv -c constraints.txt .[dev]
	@rm -rf build

test:
	$(VENV_PATH)/bin/pytest --cov=src

lint:
	@echo "\n>>> Code type checks (mypy)..."
	$(VENV_PATH)/bin/mypy src tests

	@echo "\n>>> Code format checks (RUFF)..."
	$(VENV_PATH)/bin/ruff format --check src tests

	@echo "\n>>> Code lint checks (RUFF)..."
	$(VENV_PATH)/bin/ruff check src tests

	@echo "\n>>> Dependency vulnerability checks (pip-audit)..."
	$(VENV_PATH)/bin/pip-audit --cache-dir .cache/.audit_cache

lint-fix:
	$(VENV_PATH)/bin/ruff format
	$(VENV_PATH)/bin/ruff check --fix

update-lockfile:
	@echo "Updating lock file (constraints.txt)..."
	$(VENV_PATH)/bin/pip-compile --all-build-deps --all-extras --strip-extras \
		--output-file=constraints.txt pyproject.toml
	make build

all: build test lint

# run jupyer locally
start:
	$(VENV_PATH)/bin/jupyter lab --port 8888 --NotebookApp.iopub_data_rate_limit=1.0e10

clean:
	rm -rf $(VENV_PATH)
	rm -rf build .cache .coverage

# install required tools
prepare:
	@echo "Install pyenv to manage python installations..."
	brew install pyenv

	make prepare-venv

# python virtual environment management
prepare-venv:
	@echo "Installing Python with pyenv (version from .python-version file)..."
	pyenv install -s

	@echo "Preparing Python virtual environment at $(VENV_PATH)..."
	pyenv exec python -m venv $(VENV_PATH)

venv-activate:
	@echo "run 'source .venv/bin/activate' manually"
