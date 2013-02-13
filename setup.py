#!/usr/bin/env python

from codecs import getencoder
from setuptools import setup

import spark

modules = ['spark']

setup(
	name = 'spark',
	version = spark.__version_string__,
	description = 'tool to create single line spark graphs',
	author = 'Mattijs Ugen',
	author_email = getencoder('rot-13')('tvguho+fcnex@nxnvqvbg.arg')[0],
	url = 'https://github.com/akaIDIOT/Spark',
	py_modules = modules,
	scripts = ['spark']
)

