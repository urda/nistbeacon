.PHONY: travis
travis: pep8 pylint unittest integration dogfood version-check

.PHONY: clean
clean:
	rm -rf ./.cache/ ./tests/.cache/ ./htmlcov/ .coverage

.PHONY: dogfood
dogfood:
	./scripts/dogfood.py

.PHONY: integration
integration:
	py.test ./tests/integration/

.PHONY: pep8
pep8:
	pep8 --verbose ./nistbeacon/*.py ./scripts/*.py ./tests/*.py

.PHONY: pylint
pylint:
	pylint --rcfile=./.pylintrc --reports=y --output-format=text nistbeacon

.PHONY: unittest
unittest:
	py.test --cov nistbeacon --cov-report html ./tests/unit/

.PHONY: version-check
version-check:
	./scripts/version_manager.py check
