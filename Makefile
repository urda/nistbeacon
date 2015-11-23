.PHONY: test

all:

test:
	py.test -r fEsxXw --verbose --cov py_nist_beacon --cov-report html
