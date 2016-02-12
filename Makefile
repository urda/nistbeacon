.PHONY: travis
travis: pep8 pylint unittest integration version-check

.PHONY: clean
clean:
	rm -rf ./.cache/ ./tests/.cache/ ./htmlcov/ .coverage

.PHONY: integration
integration:
	py.test ./tests/integration/

.PHONY: pep8
pep8:
	pep8 --verbose ./nistbeacon/* ./scripts/* ./tests/*

.PHONY: pylint
pylint:
	pylint --rcfile=./.pylintrc --reports=y --output-format=text nistbeacon

.PHONY: unittest
unittest:
	py.test --cov nistbeacon --cov-report html ./tests/unit/

.PHONY: version-check
version-check:
	./scripts/version_manager.py check
