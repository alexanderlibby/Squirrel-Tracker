from django.core.management.base import BaseCommand
from sightings.models import Sighting

import csv
import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=str)

    def handle(self, *args, **kwargs):
        csv_path = kwargs['csv_path']
        print("Try to read a csv file from", csv_path)
        try:
            with open(csv_path) as f:
                csv_dict = csv.DictReader(f)
                print("Reading...")
                count = 0
                for row in csv_dict:
                    # Create Sighting instance and use row to fill data
                    try:
                        sighting = Sighting(
                            latitude=float(row['Y']),
                            longitude=float(row['X']),
                            unique_squirrel_id=row['Unique Squirrel ID'],
                            shift=row['Shift'],
                            date=datetime.date(
                                int(row['Date'][4:]), int(row['Date'][:2]), int(row['Date'][2:4])),
                            age=row['Age'],
                            primary_fur_color=row['Primary Fur Color'],
                            location=row['Location'],
                            specific_location=row['Specific Location'],
                            running=(row['Running'].upper() == 'TRUE'),
                            chasing=(row['Chasing'].upper() == 'TRUE'),
                            climbing=(row['Climbing'].upper() == 'TRUE'),
                            eating=(row['Eating'].upper() == 'TRUE'),
                            foraging=(row['Foraging'].upper() == 'TRUE'),
                            other_activities=row['Other Activities'],
                            kuks=(row['Kuks'].upper() == 'TRUE'),
                            quaas=(row['Quaas'].upper() == 'TRUE'),
                            moans=(row['Moans'].upper() == 'TRUE'),
                            tail_flags=(row['Tail flags'].upper() == 'TRUE'),
                            tail_twitches=(
                                row['Tail twitches'].upper() == 'TRUE'),
                            approaches=(row['Approaches'].upper() == 'TRUE'),
                            indifferent=(row['Indifferent'].upper() == 'TRUE'),
                            runs_from=(row['Runs from'].upper() == 'TRUE'),
                        )
                        # Add this row to the database
                        sighting.save()
                        count += 1
                    except:
                        print('Cannot add', row['Unique Squirrel ID'])

                print('DONE. Added', count, 'sightings')
        except csv.Error as e:
            print(e)
            print('Please recheck your file format')
        except TypeError as e:
            print(e)
            print('There are some row with incorrect type')
