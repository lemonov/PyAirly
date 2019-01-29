#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist')
    os.system('twine upload dist/*')
    sys.exit()

setup(name='pyairly',
      version='1.0',
      license='Apache 2.0',
      url='https://github.com/lemonov/PyAirly',
      install_requires=[
          'requests',
      ],
      py_modules=['pyairly'],
      python_requires='>=3'
      )
