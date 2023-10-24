from django.core.management.base import BaseCommand
from main.models import Product

class Command(BaseCommand):
    help = "Get product by id."

    def add_arguments(self, parser):
        parser.add_argument('id', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        product = Product.objects.get(id=id)
        self.stdout.write(f'{product}')