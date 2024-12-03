from django.core.management.base import BaseCommand, CommandParser


# Proposed command = python manage.py greeting john
# proposed output = Hi {name}, Good morning
class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser):
        #pass the argument and is a function
        parser.add_argument('name', type=str, help='Specifies user name')

    def handle(self, *args, **kwargs):
        # write the logic
        name = kwargs['name']
        greeting = f'Hi {name}, Good Morning!'
        self.stdout.write(self.style.SUCCESS(greeting))
        #self.stderr.write(greeting), to show error