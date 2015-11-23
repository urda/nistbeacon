.PHONY: pep8 test

all:

pep8:
	pep8 ./py_nist_beacon/*.py ./tests/*.py

test:
	py.test -r fEsxXw --verbose --cov py_nist_beacon --cov-report html
