VERSION = $(shell python setup.py version)

PACKAGE = ci-buildbot

#======================================================================

clean:
	rm -rf *.tar.gz dist *.egg-info *.rpm
	find . -name "__pycache__" -exec rm -rf '{}' ';'

version:
	@echo $(VERSION)

dist: clean
	@python setup.py sdist

