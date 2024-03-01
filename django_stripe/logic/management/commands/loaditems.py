import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from logic.models import Item


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, 'logic/management/commands/items.csv'), 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            items = []
            for row in reader:
                items.append(Item(
                    name=row[0],
                    description=row[1],
                    price=float(row[2]),
                    currency=row[3]
                ))
            Item.objects.bulk_create(items)