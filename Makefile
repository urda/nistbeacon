.PHONY: help
help: # Show this help screen
	@ack '^[a-zA-Z_-]+:.*?# .*$$' $(MAKEFILE_LIST) |\
	sort |\
	awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'


.PHONY: build
build: test clean build-package # Clean, Test, and Build the package


.PHONY: build-package
build-package: # Build 'sdist' for this package
	python setup.py sdist


.PHONY: test
test: pep8 pylint unittest integration version-check # Run the full Travis CI testing suite


.PHONY: clean
clean: # Clean up build, test, and other project artifacts
	rm -rf \
	./.cache \
	./*.egg-info \
	./build \
	./dist \
	./htmlcov \
	.coverage \
	coverage.xml \
	&& \
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf \
	&& :


.PHONY: docs
docs: # Build the documentation
	pushd ./sphinx && \
	make clean && \
	make html && \
	popd && \
	rsync -av --delete sphinx/_build/html/ docs/
	:


.PHONY: integration
integration: # Run only integration tests
	py.test ./tests/integration/


.PHONY: pep8
pep8: # Run pep8 against project files
	pep8 --verbose ./nistbeacon/* ./scripts/* ./tests/*


.PHONY: publish
publish: build # Build, sign, and publish the package
	twine upload dist/* --sign -r pypi


.PHONY: pylint
pylint: # Run pylint against project files
	pylint --rcfile=./.pylintrc --reports=y --output-format=text nistbeacon


.PHONY: unittest
unittest: # Run only unit tests
	py.test --cov nistbeacon --cov-report html ./tests/unit/


.PHONY: version-check
version-check: # Verify the project version string is correct across the project
	./scripts/version_manager.py check
