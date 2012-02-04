import os
import sys
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from .settings import DJANGO_ENV, DJANGO_ENV_REQUIREMENTS
from .settings import DJANGO_ENV_AUTOUPDATE

VERSION = "0.1"

PROJECT_PATH = os.path.abspath('.')

       # os.path.dirname(os.path.normpath(
       #             os.sys.modules[settings].__file__))

path = getattr(settings, 'DJANGO_ENV', DJANGO_ENV)

if not os.path.isabs(path):
    path = os.path.join(PROJECT_PATH, path)


def setup(autocreate=False):
    global path
    if not os.path.isdir(path):
        print ' * Path (%s) not exists.' % path
        if autocreate:
            create()
        else:
            print ' * NOT autocreating environment'
            return False
    return activate()


def activate():
    global path
    print ' * SET UP DJANGO ENV TO %s' % path
    try:
        activate_this = os.path.join(path, 'bin', 'activate_this.py')
        execfile(activate_this, dict(__file__=activate_this))
    except:
        print 'Error while activating environment %s' % path
        return


def create():
    global path
    import virtualenv as ve
    if os.path.isdir(path):
        print 'Path with environment (%s) exist. If you want to new run '\
              ' `env_delete` first, or use --force' % path
        return
    print ' * Creating NEW environment in %s' % path
    ve.create_environment(path,
                          site_packages=True,
                          clear=True,
                         )
    if getattr(settings, 'DJANGO_ENV_AUTOUPDATE', DJANGO_ENV_AUTOUPDATE):
        update()


def update(upgrade=False):
    global path, PROJECT_PATH
    if not os.path.isdir(path):
        print 'Path with environment (%s) not exist. Run `env_create` first'
        return
    print ' * Updating environment in %s' % path
    req = os.path.join(PROJECT_PATH,
                       getattr(settings, 'DJANGO_ENV_REQUIREMENTS',
                                          DJANGO_ENV_REQUIREMENTS))
    import virtualenv as ve
    print ' * Updating pip packages from %s' % req
    from pip.baseparser import parser
    import pip.commands.install
    i = pip.commands.install.InstallCommand()
    params = ['install', '-r', req]
    if upgrade:
        params.append('-U')
    opt, args = parser.parse_args(params)
    i.main(args, args[1:], opt)


def delete():
    global path
    print ' * Deleting environment in %s' % path
    if not os.path.isdir(path):
        print 'Path with environment (%s) not exist. Nothing to do.'
        return
    import shutil
    shutil.rmtree(path)
