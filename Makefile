.PHONY: travis
travis: test pep8 dogfood-debug version-check

.PHONY: travis-nightly
travis-nightly: test dogfood-debug version-check

.PHONY: clean
clean:
	rm -rf ./.cache/ ./tests/.cache/ ./htmlcov/ .coverage

.PHONY: dogfood
dogfood:
	./scripts/dogfood.py

.PHONY: dogfood-debug
dogfood-debug:
	./scripts/dogfood.py --debug

.PHONY: pep8
pep8:
	pep8 ./py_nist_beacon/*.py ./scripts/*.py ./tests/*.py

.PHONY: test
test:
	py.test -r fEsxXw --verbose --cov py_nist_beacon --cov-report html

.PHONY version-check
version-check:
	./scripts/version_manager.py check
