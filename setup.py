#!/usr/bin/env python3.6
import os

from setuptools import setup, find_packages

__author__ = 'Simone Pandolfi <simopandolfi@gmail.com>'
__version__ = (1, 0, 0)

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyjsonmapper',
    version='0.1',
    scripts=[filename for filename in os.listdir() if filename.endswith('.py')],
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    # metadata to display on PyPI
    author="Simone Pandolfi",
    author_email="simopandolfi@gmail.com",
    description="A simple and hackable mapper from json to python objects... and viceversa!",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="json mapper",
    url="https://github.com/simongsr/pyjsonmapper",
    project_urls={},
    classifiers=[
        'License :: GNU General Public License v3.0'
    ]
)
