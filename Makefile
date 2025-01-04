build:
	TARGET=build make run-all

test:
	TARGET=test make run-all

lint:
	TARGET=lint make run-all

clean:
	TARGET=clean make run-all

all: build test lint

run-all:
	@echo "\nRunning target '$$TARGET' on all packages..."
	@find . -mindepth 2 -name Makefile -execdir sh -c "echo '\n>> Running $$(basename $$(pwd)):$$TARGET' && make $$TARGET" \;
