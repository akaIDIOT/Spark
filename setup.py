#!/usr/bin/env python

from setuptools import setup

import spark

modules = ['spark']

setup(
	name = 'spark',
	version = spark.__version_string__,
	description = 'tool to create single line spark graphs',
	author = 'Mattijs Ugen',
	author_email = 'githup+spark@mattijs-ugen.nl',
	url = 'https://github.com/akaIDIOT/Spark',
	py_modules = modules,
	scripts = ['spark.py']
)

