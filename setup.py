#!/usr/bin/env python
# encoding: utf-8
from distutils.core import setup
from os import path 

from env import VERSION

setup(author="Tomek Czyż",
      author_email='tomekczyz@gmail.com',
      description='Automaticly manages virtualenv for django project',
      long_description=open('readme').read(),
      license="BSD",
      platforms='OS Independent',
      name="django-env",
      url="http://github.com/spinus/django-env",
      classifiers=[
           "Environment :: Web Environment",
           "Framework :: Django",
           "Intended Audience :: Developers",
           "License :: OSI Approved :: BSD License",
           "Operating System :: OS Independent",
           "Programming Language :: Python",
           'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      version=VERSION,
      keywords="django virtualenv managment",
      packages=['env','env.management','env.management.commands'],
      )
