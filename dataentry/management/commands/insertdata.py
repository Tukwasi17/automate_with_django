from django.core.management.base import BaseCommand
from dataentry.models import Student

# i want to add some data to the database using the custom command

class Command(BaseCommand):
    help = 'it will insert data to the database'

    def handle(self, *args, **kwargs):
        # logic goes here
        dataset = [
            {'roll_no': 1002, 'name': 'Doe', 'age':20},
            {'roll_no': 1003, 'name': 'Ada', 'age':22},
            {'roll_no': 1004, 'name': 'Obioma', 'age':24},
            {'roll_no': 1005, 'name': 'Kindness', 'age':26},
            {'roll_no': 1006, 'name': 'Chiboy', 'age':29},
            {'roll_no': 1007, 'name': 'Agu', 'age':31},
        ]
        
        for data in dataset:
            #print(data['name'])
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists() #this is a query

            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no} already exists!'))
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))    
        
        
        
        # add 1 data
        """
        Student.objects.create(roll_no=1001, name='Tukwasi', age=17)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
        """