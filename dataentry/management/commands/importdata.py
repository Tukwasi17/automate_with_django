from django.core.management.base import BaseCommand, CommandParser, CommandError
#from dataentry.models import Student
from django.apps import apps
from dataentry.utils import check_csv_errors
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

        model = check_csv_errors(file_path, model_name)

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
                #Student.objects.create(**row)
                #print(row)
            #print(reader)
        #print(file_path)
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))