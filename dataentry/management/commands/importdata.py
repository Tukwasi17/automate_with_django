from django.core.management.base import BaseCommand, CommandParser, CommandError
#from dataentry.models import Student
from django.apps import apps
import csv

# Proposed command - python manage.py importdata file_path and model_name

class Command(BaseCommand):
    help = "Import data from csv file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model')#new one added


    def handle(self, *args, **kwargs):
        #logic goes here
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        # Search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            # try search for the model
            try:
                model = apps.get_model(app_config.label, model_name)
                break # Stop searching once the model is found
            except LookupError:
                continue # model not found in the app, continue seraching the next app

        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app!')
                

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
                #Student.objects.create(**row)
                #print(row)
            #print(reader)
        #print(file_path)
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))