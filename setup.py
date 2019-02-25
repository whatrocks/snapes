#!/usr/bin/env pytho

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
        "beautifulsoup4",
        "requests",
        "redis",
        "flask"
    ],
    tests_require=[],
    extras_require={
        "dev": [
            "pytest",
            "ujson",
        ]
    },
    entry_points={}
)