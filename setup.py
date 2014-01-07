#! /usr/bin/env python

from setuptools import setup

setup(name="django-dont-vary-on-everything",
      version="0.1",
      author="Dennis Schwertel",
      author_email="s@digitalkultur.net",
      packages=['django_dont_vary_on_everything'],
      license = 'GPLv3',
      description = "Library for Django to remove all vary headers",
      install_requires = [ 'django' ],
)
