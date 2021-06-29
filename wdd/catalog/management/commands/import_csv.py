import csv
from pathlib import Path
from django.core.management import BaseCommand
from catalog.models import Device


class Command(BaseCommand):
    help = 'Load a csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str)

    def handle(self, *args, **kwargs):
        base_csv_path = 'import_datafiles'
        app_path = Path(__file__).resolve().parents[2]
        file_name = kwargs['name']
        file_path = app_path / base_csv_path / file_name
        print(file_path)
        device_counter = 0
        with open(file_path, 'rt') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Device.objects.create(**row)
                device_counter += 1

        print(f'Total devices was created: {device_counter}')
