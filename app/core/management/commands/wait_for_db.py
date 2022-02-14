import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until datbase is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for datbase...')
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections['default']
            except (OperationalError):
                self.stdout.write('Database connection unavailable')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
