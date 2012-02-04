from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
import env


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--force', '-f', dest='force',
            action='store_true',
            default=False,
            help='Delete environment before recreating'),
    )
    help = 'Create environment in %s' % env.path

    def handle(self, **options):
        if options['force']:
            env.delete()
        env.create()
