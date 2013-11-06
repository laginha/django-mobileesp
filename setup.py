#!/usr/bin/env python
# encoding: utf-8
from setuptools import setup, find_packages

setup(
    name             = 'Django-Mobileesp',
    version          = '1.0.0',
    author           = "Diogo Laginha",
    url              = 'https://github.com/laginha/django-mobileesp',
    description      = "Detect request's mobile user agents using the mobileesp lib.",
    packages         = find_packages(where='src'),
    package_dir      = {'': 'src'},
    install_requires = ['django'],
    extras_require   = {},
    zip_safe         = False,
)
