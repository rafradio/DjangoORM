from django.core.management.base import BaseCommand
from main.models import Newnote
from main.models import Product

class Command(BaseCommand):
    help = "Print 'Hello world!' to output."

    def handle(self, *args, **kwargs):
        mynote = Newnote(title='test', body='test', date='2023-10-23')
        mynote.save()
        self.stdout.write('My First commond!')
        # prod = Product()
        # prod.save()
