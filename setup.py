# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in panoptic/__init__.py
from panoptic import __version__ as version

setup(
	name='panoptic',
	version=version,
	description='Tracking FRT Across the Country',
	author='Internet Freedom Foundation',
	author_email='panoptic@internetfreedom.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
