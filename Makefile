.PHONY: dev-setup ## Install development dependencies
dev-setup:
	pip install -e ".[dev]"

.PHONY: install-dev
install-dev: dev-setup  # Alias install-dev -> dev-setup

.PHONY: tests
tests:
	py.test -vv

.PHONY: test
test: tests  # Alias test -> tests

.PHONY: format
format:
	black graphene_t2 tests setup.py

.PHONY: fmt
fmt:: format
