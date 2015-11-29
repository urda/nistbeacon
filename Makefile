.PHONY: travis clean dogfood pep8 test version-check

travis: test pep8 dogfood version-check

clean:
	rm -rf ./.cache/ ./tests/.cache/ ./htmlcov/ .coverage

dogfood:
	./scripts/dogfood.py

pep8:
	pep8 ./py_nist_beacon/*.py ./scripts/*.py ./tests/*.py

test:
	py.test -r fEsxXw --verbose --cov py_nist_beacon --cov-report html

version-check:
	./scripts/version_manager.py check
