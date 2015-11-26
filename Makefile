.PHONY: register upload prod-register prod-upload clean pep8 test

all: pep8 test clean

register:
	python setup.py register -r pypitest

upload:
	python setup.py sdist upload -r pypitest

prod-register:
	python setup.py register -r pypi

prod-upload:
	python setup.py sdist upload -r pypi

clean:
	rm -rf ./.cache/ ./tests/.cache/ ./htmlcov/ .coverage

pep8:
	pep8 ./py_nist_beacon/*.py ./scripts/*.py ./tests/*.py

test:
	py.test -r fEsxXw --verbose --cov py_nist_beacon --cov-report html
