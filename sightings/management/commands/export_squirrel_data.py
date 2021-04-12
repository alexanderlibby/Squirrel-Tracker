from django.core.management.base import BaseCommand
  
import csv
import pandas as pd
from sightings.models import Sighting

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_path')

    def handle(self, *args, **options):
        path = options['csv_path']
        sightings = Sighting.objects.all()
        df = pd.DataFrame(sightings.values())
        df.to_csv(path)

        print('Sightings exported to: ', path)
