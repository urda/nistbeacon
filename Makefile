.PHONY: help
help: # Show this help screen
	@ack '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) |\
	sort |\
	awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: test
test: pep8 pylint unittest integration version-check # Run the full Travis CI testing suite

.PHONY: clean
clean: # Clean up test artificats
	rm -rf ./.cache/ ./tests/.cache/ ./htmlcov/ .coverage

.PHONY: docs
docs: # Build the documentation
	cd ./docs && make html

.PHONY: integration
integration: # Run only integration tests
	py.test ./tests/integration/

.PHONY: pep8
pep8: # Run pep8 against project files
	pep8 --verbose ./nistbeacon/* ./scripts/* ./tests/*

.PHONY: pylint
pylint: # Run pylint against project files
	pylint --rcfile=./.pylintrc --reports=y --output-format=text nistbeacon

.PHONY: unittest
unittest: # Run only unit tests
	py.test --cov nistbeacon --cov-report html ./tests/unit/

.PHONY: version-check
version-check: # Verify the project version string is correct across the project
	./scripts/version_manager.py check
