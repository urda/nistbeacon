.PHONY: clean pep8 test

all:

clean:
	rm -rf ./.cache/ ./htmlcov/ .coverage

pep8:
	pep8 ./py_nist_beacon/*.py ./tests/*.py

test:
	py.test -r fEsxXw --verbose --cov py_nist_beacon --cov-report html
