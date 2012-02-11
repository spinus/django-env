__doc__='''
Settings.py
-----------

You can set number of settings:
'''

#: Directory's name of virtualenv.
#: If the name is *relative name* it is appended to
#: *project's path*, if the name is *absolute name* (starts with /), 
#: is is set as is for virtualenv's directory.
DJANGO_ENV_NAME = 'py_env'

#: During `env_update` it is used *pip* for installing packages, you can add
#: here additional arguments like *-i* or *-f*. `-U` can be set dynamicaly by
#: adding `--upgrade` to `env_update`.
DJANGO_ENV_UPDATE_PIP_ARGUMENTS = []

#: Name of file with requirements. If this path is relative is appended to 
#: project's path, else it is set as absolute.
DJANGO_ENV_UPDATE_REQUIREMENTS = 'requirements.pip'

#: When doing `env_create`, should be run `env_update` after it.
DJANGO_ENV_CREATE_AUTOUPDATE = False

#: When doing `env_create`, should it *connect* global *site-packages*.
DJANGO_ENV_CREATE_SITEPACKAGES = False
