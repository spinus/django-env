django-env
==========

Installation
------------

.. warning::

    You have to consider where to place this package because it has to be
    importable "outside" your project. Probably best place for it exists in
    project directory (or your "lib" directory) or in system-wide packages'
    place.

Simplest way is to do (system-wide):

.. sourcecode:: bash

    pip install django-env

or using archive

.. sourcecode:: bash

    tar xf django-env*
    cd django-env*
    python setup.py install

or place installed egg in project's directory.

Configuration
-------------

Firstly, you have some options in `settings.py`:

.. automodule:: env.settings
    
.. note:: Project's directory is the same where `manage.py` and `settings.py` lives.

INSTALLED_APPS
~~~~~~~~~~~~~~

.. note:: It is just cosmetic change to display command in `manage.py help`.

Add `env` to `INSTALLED_APPS`:

.. sourcecode:: python

    INSTALLED_APPS += ('env', )

project setup
~~~~~~~~~~~~~

How to activate the environment?
Example:

.. sourcecode:: python

    import env

I suggest to place it in `manage.py` at the top. 

How it works?
-------------

It just grab control from `manage.py` (if you import it) and check the argument line.
If you passed one of `django-env` commands, it do what is needed and exit; else
it pass control to `manage.py` to parse other args.

Usage
-----

Target of this project is automating in creating project environment.

This app gives you some additional `manage.py` commands:

env_create [--force]
  create environment (and optionally do `env_update` - it depends on
  DJANGO_ENV_AUTOUPDATE variable in `settings.py`)

env_update [--upgrade]
    install packages from DJANGO_ENV_REQUIREMENTS file to current environment
    via `pip install -r`, or if you provide `--upgrade` it runs `pip install -U
    -r`.

    You can pass other arguments to `pip`, see `settings.py`.

env_remove
    simply deletes environments directory.

TODO
----

* `py_env`/last_update - show last update date - monitoring feature

.. todolist::

.. include:: changes.rst
