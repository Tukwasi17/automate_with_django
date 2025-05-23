from django.core.management.base import BaseCommand, CommandParser, CommandError
#from dataentry.models import Student
from django.apps import apps
import csv

from django.db import DataError

# Proposed command - python manage.py importdata file_path and model_name

class Command(BaseCommand):
    help = "Import data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model (e.g. Student)')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        # Look for the model in all installed apps
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue

        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app!')

        # Define field mappings from CSV headers to model fields
        field_maps = {
            'Student': {
                'Roll No': 'roll_no',
                'Name': 'name',
                'Age': 'age',
            },
            # Add more mappings here for other models as needed
            'Employee': {
                'employee_id': 'employee_id',
                'employee_name': 'employee_name',
                'designation': 'designation',
                'salary': 'salary',
                'retirement': 'retirement',
                'other_benefits': 'other_benefits',
                'total_benefits': 'total_benefits',
                'total_compensation': 'total_compensation',
            },
        }

        if model_name not in field_maps:
            raise CommandError(f'Field map not defined for model "{model_name}"')

        model_field_map = field_maps[model_name]

        model_fields = [field.name for field in model._meta.fields if field.name != 'id']
        print("Model fields:", model_fields)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                csv_header = reader.fieldnames
                print("CSV headers:", csv_header)

                # Map the CSV headers and compare
                mapped_fields = [model_field_map.get(col) for col in csv_header if col in model_field_map]
                if sorted(mapped_fields) != sorted(model_fields):
                    raise DataError(f"CSV fields {csv_header} don't match model fields {model_fields}.")

                for row in reader:
                    cleaned_row = {
                        model_field_map[k]: v for k, v in row.items() if k in model_field_map
                    }
                    model.objects.create(**cleaned_row)

        except Exception as e:
            raise CommandError(f"Failed to import data: {str(e)}")

        self.stdout.write(self.style.SUCCESS('✅ Data imported successfully!'))





""" class Command(BaseCommand):
    help = "Import data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model (e.g. Student)')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        # Look for the model in all installed apps
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break
            except LookupError:
                continue

        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app!')

        # Define field mappings from CSV headers to model fields
        field_maps = {
            'Student': {
                'Roll No': 'roll_no',
                'Name': 'name',
                'Age': 'age',
            },
            # Add more mappings here for other models as needed
        }

        if model_name not in field_maps:
            raise CommandError(f'Field map not defined for model "{model_name}"')

        model_field_map = field_maps[model_name]

        # Compare csv header with model's field names
        # get all the field names of the model that we found
        model_fields = [field.name for field in model._meta.fields if field.name != 'id']
        print(model_fields)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                csv_header = reader.fieldnames
                #compare csv header with model's field name
                if csv_header != model_fields:
                    raise DataError(f"CSV file doesn't match with the {model_name} table field")
                for row in reader:
                    cleaned_row = {
                        model_field_map[k]: v for k, v in row.items() if k in model_field_map
                    }
                    model.objects.create(**cleaned_row)
        except Exception as e:
            raise CommandError(f"Failed to import data: {str(e)}")

        self.stdout.write(self.style.SUCCESS('✅ Data imported successfully!'))

 
 """




""" class Command(BaseCommand):
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

        # Compare csv header with model's field names
        # get all the field names of the model that we found
        model_fields = [field.name for field in model._meta.fields if field.name != 'id']
        print(model_fields)        

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            #compare csv header with model's field name
            if sorted(csv_header) != sorted(model_fields):
                    raise DataError(f"CSV file doesn't match with the {model_name} table field")
            for row in reader:
                model.objects.create(**row)
                #Student.objects.create(**row)
                #print(row)
            #print(reader)
        #print(file_path)
        self.stdout.write(self.style.SUCCESS('Data imported successfully!')) """