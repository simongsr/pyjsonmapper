#!/usr/bin/env python3.6
import os

from setuptools import setup, find_packages

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)

setup(
    name="pyjsonmapper",
    version="0.1",
    packages=find_packages(),
    scripts=[filename for filename in os.listdir() if filename.endswith('.py')],
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata to display on PyPI
    author="Simone Pandolfi",
    author_email="simopandolfi@gmail.com",
    description="A simple and hackable mapper from json to python objects... and viceversa!",
    keywords="json mapper",
    url="https://github.com/simongsr/pyjsonmapper",
    project_urls={},
    classifiers=[
        'License :: GNU General Public License v3.0'
    ]
)
