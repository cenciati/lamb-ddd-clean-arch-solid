SHELL = /bin/bash
PYTHON := python3 -m
POETRY := poetry run
FILES_PATH := src
TESTS_PATH := tests

.PHONY: help lint test test_not_e2e setup clean
.ONESHELL: setup clean

help: ## Display commands help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ Development
lint: ## Run linters and formatters
	${POETRY} ${PYTHON} isort ${FILES_PATH} ${TESTS_PATH}
	${POETRY} ${PYTHON} black ${FILES_PATH} ${TESTS_PATH}
	${POETRY} ${PYTHON} pylint ${FILES_PATH} ${TESTS_PATH}
	${POETRY} ${PYTHON} flake8 ${FILES_PATH} ${TESTS_PATH}

test: ## Run all tests
	${POETRY} ${PYTHON} pytest ${TESTS_PATH}

test_not_e2e: ## Run only unit and integration tests
	${POETRY} ${PYTHON} pytest ${TESTS_PATH} -k "not e2e"

##@ Environment
setup: ## Install dependencies and setup docker-compose.
	echo "placeholder"

clean: setup ## Cleans everything installed.
	echo "placeholder"