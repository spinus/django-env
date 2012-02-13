import os
import sys

from .settings import DJANGO_ENV_NAME
from .settings import DJANGO_ENV_UPDATE_PIP_ARGUMENTS
from .settings import DJANGO_ENV_UPDATE_REQUIREMENTS
from .settings import DJANGO_ENV_CREATE_AUTOUPDATE
from .settings import DJANGO_ENV_CREATE_SITEPACKAGES

from logging import getLogger
import logging

log = getLogger('django-env')
log.setLevel(logging.INFO)

stdout_formatter = logging.Formatter(" * [%(levelname)-7s] - %(message)s")
stdout_handler = logging.StreamHandler()
stdout_handler.setFormatter(stdout_formatter)

log.addHandler(stdout_handler)
log.debug('-- DJANGO-ENV START --')
log.debug('settings: %s' % settings)

VERSION = "0.2.1"

# SET PATHS

PROJECT_PATH = os.path.abspath('.')
log.debug('project base: %s' % PROJECT_PATH)

path = getattr(settings, 'DJANGO_ENV_NAME', DJANGO_ENV_NAME)

if not os.path.isabs(path):
    path = os.path.join(PROJECT_PATH, path)

# Try to load projects settings

try:
    settings = __import__('settings')
except Exception as e:
    log.error("Could not load project settings (project dir: %s)" %
              (PROJECT_PATH))

log.debug('django-env: %s' % path)
log.debug('settings: %s' % settings)


# DEFINE FUNCTIONS

def activate():
    '''
    Activate environment - call env/bin/activate_this.py.
    '''
    global path
    try:
        if not os.path.isdir(path):
            raise Exception('Path with environment (%s) not exists' % path)
        activate_this = os.path.join(path, 'bin', 'activate_this.py')
        execfile(activate_this, dict(__file__=activate_this))
        log.info('Django env set to: %s' % path)
    except Exception as e:
        #log.exception("%s" % e)
        log.error("%s" % e)
        log.error('ERROR while activating environment %s' % path)
        return


def create():
    '''
    If path with environment not exists, create new one.
    If path exists, you can force recreating by passing `--force`.
    If *DJANGO_ENV_CREATE_AUTOUPDATE* is set to *True*, call `env_update`.
    '''
    global path
    import virtualenv as ve
    if os.path.isdir(path):
        log.error('Path with environment (%s) exist. If you want to new run '\
              ' `env_delete` first, or use --force' % path)
        return
    log.info(' * Creating NEW environment in %s' % path)
    ve.create_environment(path,
                          site_packages=True,
                          clear=True,
                         )
    if getattr(settings, 'DJANGO_ENV_CREATE_AUTOUPDATE',
               DJANGO_ENV_CREATE_AUTOUPDATE):
        log.debug('autoupdate: on')
        update()
    else:
        log.debug('autoupdate: off')


def update(upgrade=False):
    '''
    Install packages in virtual environment (call pip install -r
    DJANGO_ENV_UPDATE_REQUIREMENTS)
    '''
    global path, PROJECT_PATH
    if not os.path.isdir(path):
        log.error('Path with environment (%s) not exist. Run `env_create` '
                  'first')
        return
    req_name = getattr(settings, 'DJANGO_ENV_UPDATE_REQUIREMENTS',
                                  DJANGO_ENV_UPDATE_REQUIREMENTS)
    req = req_name 

    if os.path.isabs(req_name):
        req = req_name
    else:
        req = os.path.join(PROJECT_PATH, req_name)

    log.info('Updating environment in: %s' % path)
    import virtualenv as ve
    log.info('Updating pip packages from: %s' % req)
    try:
        from pip.baseparser import parser
        import pip.commands.install
        i = pip.commands.install.InstallCommand()
        params = ['install', '-r', req]
        params.extend(
                 getattr(settings, 'DJANGO_ENV_UPDATE_PIP_ARGUMENTS',
                         DJANGO_ENV_UPDATE_PIP_ARGUMENTS)
        )

        if upgrade:
            params.append('-U')
        opt, args = parser.parse_args(params)
        opt.venv = path
        opt.venv_base = path
        opt.respect_venv = True
        opt.require_venv = True
        opt.no_input = True
        opt.verbose = 2
        log.debug('PIP parsed opts: %s' % opt)
        log.debug('PIP parsed args: %s' % args)

        log.debug('PIP exec: %s' % i.main(args, args[1:], opt))
    except Exception as e:
        log.exception("Error in PIP: %s", e)
        return


def delete():
    '''
    If virtual environment's directory exists, delete it.
    '''
    global path
    log.info('Deleting environment in %s' % path)
    if not os.path.isdir(path):
        log.info('Path with environment (%s) not exist. Nothing to do.' % path)
        return
    import shutil
    shutil.rmtree(path)


##
# MAIN PART
##

try:
    if sys.argv[1] == 'env_create':
        if '--force' in sys.argv[1:]:
            log.info('Creating env with --force')
            delete()
        create()
        sys.exit(0)
    elif sys.argv[1] == 'env_update':
        activate()
        upgrade = True if '--upgrade' in sys.argv[1:] else False
        update(upgrade)
        sys.exit(0)
    elif sys.argv[1] == 'env_delete':
        delete()
        sys.exit(0)
        #: .. todo:: env_make_bundle
        #: .. todo:: env_deploy_bundle
except IndexError:
    # pass control to django if no arguments
    pass
log.debug('Trying to activate django-env')
activate()
