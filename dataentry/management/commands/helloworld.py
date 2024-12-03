from typing import Any
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prints Hello World"

    def handle(self, *args, **kwargs):
        #we write the logic
        self.stdout.write('Hello World')