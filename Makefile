VERSION = $(shell python setup.py version)

PACKAGE = ci-buildbot

#======================================================================

clean:
	rm -rf *.tar.gz dist *.egg-info dist
	find . -name "__pycache__" | xargs rm -rf

version:
	@echo $(VERSION)

dist: clean
	@uv build

.PHONY: icons
icons:
	@aws s3 sync --acl public-read ./icons s3://ads-utils-icons/ci-buildbot/

release: dist
	@twine upload dist/*