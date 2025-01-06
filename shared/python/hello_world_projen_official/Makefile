PROJEN_VERSION=0.91.5
VENV_PATH = .venv

# build module
build: prepare-venv
	@echo "Project synth..."
	$(VENV_PATH)/bin/python3 .projenrc.py

	@echo "Building package..."
	$(VENV_PATH)/bin/projen compile
	$(VENV_PATH)/bin/projen package

test:
	$(VENV_PATH)/bin/projen test

lint:

all: build test lint

# run jupyer locally
clean:
	rm -rf $(VENV_PATH) .env
	rm -rf build .pytest_cache

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

	@echo "Installing Projen $(PROJEN_VERSION)..."
	$(VENV_PATH)/bin/pip3 install projen==$(PROJEN_VERSION)
