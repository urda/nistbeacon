########################################################################################################################
# Variables
########################################################################################################################


BETA_DIST = ./beta_dist
CLEAN_TARGETS = ./.cache ./*.egg-info $(BETA_DIST) $(DIST) ./build ./htmlcov .coverage coverage.xml
DIST = ./dist
GPG_ID = CA0B97334F9449EB5AFFCB93240BD54D194E3161


########################################################################################################################
# `make help` Needs to be first so it is ran when just `make` is called
########################################################################################################################


.PHONY: help
help: # Show this help screen
	@ack '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) |\
	sort -k1,1 |\
	awk 'BEGIN {FS = ":.*?# "}; {printf "\033[1m%-30s\033[0m %s\n", $$1, $$2}'


########################################################################################################################
# Linting
########################################################################################################################


.PHONY: pycodestyle
pycodestyle: # Run pycodestyle against project files
	pycodestyle --verbose ./nistbeacon/* ./scripts/* ./tests/*


.PHONY: pylint
pylint: # Run pylint against project files
	pylint --rcfile=./.pylintrc --reports=y --output-format=text nistbeacon


.PHONY: version-check
version-check: # Verify the project version string is correct across the project
	./scripts/version_manager.py check


########################################################################################################################
# Testing
########################################################################################################################


.PHONY: unittest
unittest: # Run only unit tests
	py.test --cov nistbeacon --cov-report html ./tests/unit/


.PHONY: integration
integration: # Run only integration tests
	py.test ./tests/integration/


########################################################################################################################
# Project Building
########################################################################################################################


.PHONY: build
build: build-pre build-package # Build the release package


.PHONY: build-beta
build-beta: build-pre build-beta-package # Build the beta package


.PHONY: clean
clean: # Clean up build, test, and other project artifacts
	rm -rf $(CLEAN_TARGETS) && \
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf && \
	:

#---------------------------------------------------------------------------------------------------
# Build Subcommands
#---------------------------------------------------------------------------------------------------


# Perform required pre-build steps for all build types
.PHONY: build-pre
build-pre: clean pycodestyle pylint unittest integration version-check


# Build 'sdist' and 'bdist_wheel' for this package
.PHONY: build-package
build-package:
	python setup.py sdist --dist-dir $(DIST) bdist_wheel --dist-dir $(DIST)


# Build 'sdist' and 'bdist_wheel' for the beta package
.PHONY: build-beta-package
build-beta-package:
	./scripts/version_manager.py set-beta-build && \
	./scripts/version_manager.py check && \
	python setup.py sdist --dist-dir $(BETA_DIST) bdist_wheel --dist-dir $(BETA_DIST) && \
	./scripts/version_manager.py unset-beta-build && \
	:
