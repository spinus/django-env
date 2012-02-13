
django-env
**********


Installation
============

Warning: You have to consider where to place this package because it has to
  be importable "outside" your project. Probably best place for it
  exists in project directory (or your "lib" directory) or in system-
  wide packages' place.

Simplest way is to do (system-wide):

   pip install django-env

or using archive

   tar xf django-env*
   cd django-env*
   python setup.py install

or place installed egg in project's directory.


Configuration
=============

Firstly, you have some options in *settings.py*:


Settings.py
-----------

You can set number of settings:

env.settings.DJANGO_ENV_CREATE_AUTOUPDATE = False

   When doing *env_create*, should be run *env_update* after it.

env.settings.DJANGO_ENV_CREATE_SITEPACKAGES = False

   When doing *env_create*, should it *connect* global *site-
   packages*.

env.settings.DJANGO_ENV_NAME = 'py_env'

   Directory's name of virtualenv. If the name is *relative name* it
   is appended to *project's path*, if the name is *absolute name*
   (starts with /), is is set as is for virtualenv's directory.

env.settings.DJANGO_ENV_UPDATE_PIP_ARGUMENTS = []

   During *env_update* it is used *pip* for installing packages, you
   can add here additional arguments like *-i* or *-f*. *-U* can be
   set dynamicaly by adding *--upgrade* to *env_update*.

env.settings.DJANGO_ENV_UPDATE_REQUIREMENTS = 'requirements.pip'

   Name of file with requirements. If this path is relative is
   appended to project's path, else it is set as absolute.

Note: Project's directory is the same where *manage.py* and *settings.py*
  lives.


INSTALLED_APPS
--------------

Note: It is just cosmetic change to display command in *manage.py help*.

Add *env* to *INSTALLED_APPS*:

   INSTALLED_APPS += ('env', )


project setup
-------------

How to activate the environment? Example:

   import env

I suggest to place it in *manage.py* at the top.


How it works?
=============

It just grab control from *manage.py* (if you import it) and check the
argument line. If you passed one of *django-env* commands, it do what
is needed and exit; else it pass control to *manage.py* to parse other
args.


Usage
=====

Target of this project is automating in creating project environment.

This app gives you some additional *manage.py* commands:

env_create [--force]
   create environment (and optionally do *env_update* - it depends on
   DJANGO_ENV_AUTOUPDATE variable in *settings.py*)

env_update [--upgrade]
   install packages from DJANGO_ENV_REQUIREMENTS file to current
   environment via *pip install -r*, or if you provide *--upgrade* it
   runs *pip install -U -r*.

   You can pass other arguments to *pip*, see *settings.py*.

env_remove
   simply deletes environments directory.


TODO
====

* *py_env*/last_update - show last update date - monitoring feature


Changes
*******

0.2

   * easier setup

   * added several options to 'settings.py'

   * it should work!

0.1 - init
