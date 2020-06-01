#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="ci-buildbot",
    version='0.1.0',
    description="Slack client for managing CodePipeline docker builds",
    author="Caltech IMSS ADS",
    author_email="imss-ads-staff@caltech.edu",
    packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test", "bin", "*.pyc"]),
    entry_points={
        'console_scripts': ['buildbot = ci_buildbot.cli:main']
    }
)
