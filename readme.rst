django-env
==========

Installation
------------

You have to consider where to place this package. 
Simplest way is to do:

.. sourcecode:: bash

    pip install django-env

or using archive

.. sourcecode:: bash

    tar xf django-env*
    cd django-env*
    python setup.py install

.. warning::

    But as django-env is created to managing project environment, you should
    place it at least "one level up". Good examples are `system site-packages`
    or just in your django project directory.

Configuration
-------------

settings.py
~~~~~~~~~~~

First, you have some options in `settings.py`:

DJANGO_ENV = 'py_env'

    name of the environment. If this is a name, environment will be placed
    in project directory. If it is an absolute path, it will be used instead.

DJANGO_ENV_AUTOUPDATE = False

    it tells wheter after creating (`env_create`) environment it should
    automatically install packages (run `env_update`)

DJANGO_ENV_REQUIREMENTS = 'requirements.pip'

    name of file with requirements of environments. django-env will be
    searching it in project directory.
    
    .. note:: project directory is the same where `settings.py` lives.

And of course add `env` to `INSTALLED_APPS`

.. sourcecode:: python

    INSTALLED_APPS += ('env', )

project setup
~~~~~~~~~~~~~

How to activate the environment?
Example:

.. sourcecode:: python

    from env import setup
    setup(autocreate=False)  # default

I suggest to place it in `manage.py` at the bottom:

.. sourcecode:: python

    import settings                                                                  
                                                                                     
    if __name__ == "__main__":                                                       
        execute_manager(settings)                                                    
        from env import setup                                                        
        setup()    

of if you want to auto-create environment:

.. sourcecode:: python

    import settings                                                                  
                                                                                     
    if __name__ == "__main__":                                                       
        execute_manager(settings)                                                    
        from env import setup                                                        
        setup(autocreate=True)    

.. warning::

    Generally rule of it is to load environment after reading the `settings.py`
    (optionally) and after `manage.py` executes commands (if you place it
    before, `setup()` loads the environment, and than for example you call
    `env_delete` and it will crash.

Usage
-----

Target of this project is automating in creating project environment.

This app gives you some additional `manage.py` commands:

env_create [--force]

  create environment (and optionally do `env_update` - it depends on
  DJANGO_ENV_AUTOUPDATE variable in `settings.py`)

env_update [-U|--upgrade]

    install packages from DJANGO_ENV_REQUIREMENTS file to current environment
    via `pip install -r`, or if you provide `--upgrade` it runs `pip install -U
    -r`.

env_remove

    simply deletes environments directory.

TODO
----

* `py_env`/last_update - show last update date - monitoring feature
