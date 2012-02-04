from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
import env


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--upgrade', '-U', dest='upgrade',
            action='store_true',
            default=False,
            help='Pass --upgrade parameter to pip, install everything again.'),
    )
    help = 'Update environment (install requirements) in %s' % env.path

    def handle(self, **options):
        env.update(upgrade=options['upgrade'])
