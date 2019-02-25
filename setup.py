#!/usr/bin/env python

from setuptools import find_packages, setup

__version__ = '0.1'

setup(
    name='snapes',
    version=__version__,
    description='Snapes',
    author='Charlie Harrington',
    url='https://www.charlieharrington.com',
    packages=find_packages(exclude=['*.tests']),
    setup_requires=[],
    install_requires=[
        "beautifulsoup4==4.7.1",
        "requests==2.21.0",
        "redis==3.2.0",
        "Flask==1.0.2",
        "uwsgi==2.0.18"
    ],
    tests_require=[],
    extras_require={
        "dev": [
            "flake8",
            "mypy",
            "pytest==4.3.0",
            "ujson==1.35",
        ]
    },
    entry_points={}
)