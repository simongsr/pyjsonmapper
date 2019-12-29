#!/usr/bin/env python3.6
from setuptools import setup

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)

setup(
    name="pyjsonmapper",
    version="0.1",
    description="A simple and hackable mapper from json to python objects... and viceversa!",
    author="Simone Pandolfi",
    author_email="simopandolfi@gmail.com",
    keywords="json mapper",
    classifiers=[
        'License :: GNU General Public License v3.0'
    ],
    url="https://github.com/simongsr/pyjsonmapper",
    packages=[],
    scripts=[
        '__init__.py',
        'field.py',
        'model.py',
        'validator.py',
    ],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
    },
)
