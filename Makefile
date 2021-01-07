VERSION = $(shell python setup.py version)

PACKAGE = ci-buildbot

#======================================================================

clean:
	rm -rf *.tar.gz dist *.egg-info *.rpm
	find . -name "__pycache__" | xargs rm -rf

version:
	@echo $(VERSION)

dist: clean
	@python setup.py sdist
	@python setup.py bdist_wheel --universal


.PHONY: icons
icons:
	@aws s3 sync --acl public-read ./icons s3://ads-utils-icons/ci-buildbot/

pypi: dist
	@twine upload dist/*

tox:
	# create a tox pyenv virtualenv based on 2.7.x
	# install tox and tox-pyenv in that ve
	# actiave that ve before running this
	@tox
