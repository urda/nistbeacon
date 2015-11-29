.PHONY: travis clean dogfood dogfood-debug pep8 test version-check

travis: test pep8 dogfood-debug version-check

clean:
	rm -rf ./.cache/ ./tests/.cache/ ./htmlcov/ .coverage

dogfood:
	./scripts/dogfood.py

dogfood-debug:
	./scripts/dogfood.py --debug

pep8:
	pep8 ./py_nist_beacon/*.py ./scripts/*.py ./tests/*.py

test:
	py.test -r fEsxXw --verbose --cov py_nist_beacon --cov-report html

version-check:
	./scripts/version_manager.py check
