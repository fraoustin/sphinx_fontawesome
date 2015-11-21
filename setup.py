#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
from setuptools import setup, find_packages

import sphinx_fontawesome

name = "sphinx_fontawesome"
version = sphinx_fontawesome.__version__
desc = "add directive for fontawesome in sphinx"
urlpkg = "https://github.com/fraoustin/sphinx_fontawesome"

here = os.path.abspath(os.path.dirname(__file__))

# README AND CHANGES
with open(os.path.join(here, 'README.rst')) as readme:
    with open(os.path.join(here, 'CHANGES.rst')) as changelog:
        long_description = readme.read() + '\n\n' + changelog.read()
# REQUIREMENTS
with open('REQUIREMENTS.txt') as f:
    required = f.read().splitlines()
# CLASSIFIERS
with open('CLASSIFIERS.txt') as f:
    classified = f.read().splitlines()
# AUTHORS
with open('AUTHORS.txt') as f:
    data = f.read().splitlines()
    authors = ','.join([i.split('::')[0] for i in data])
    authors_email = ','.join([i.split('::')[1] for i in data])

setup(
    name = name,
    version = version,
    packages = find_packages(),
    author = authors,
    author_email = authors_email,
    description = desc,
    long_description= long_description,
    include_package_data=True,
    install_requires=required,
    url = urlpkg,
    classifiers=classified,
)
