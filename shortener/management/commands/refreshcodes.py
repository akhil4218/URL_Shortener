from django.core.management.base import BaseCommand, CommandError

from shortener.models import yellowURL

class Command(BaseCommand):
    help = 'Refreshers all URLS'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return yellowURL.objects.refresh_shortcodes(items=options['items'])
