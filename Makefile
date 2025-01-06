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
	@find . -mindepth 2 -maxdepth 5 -name Makefile -exec sh -c \
		'cd "$$(dirname {})" && \
		PARENT_DIR=$$(basename $$(dirname $$(pwd))) && CURRENT_DIR=$$(basename $$(pwd)) && \
		echo "\n>> Running $$PARENT_DIR/$$CURRENT_DIR:[$$TARGET]" && make $$TARGET' \;

