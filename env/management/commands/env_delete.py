#from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
import env


class Command(BaseCommand):
    help = 'Delete environment in %s' % env.path

    def handle(self, **options):
        env.delete()
