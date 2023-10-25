from django.core.management.base import BaseCommand
from main.models import Product

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        data = {
            'name': "bread",
            'details': "first",
            'price': 47.88,
            'quantity': 3,
            'date_registration': "2023-10-23 23:20:51"
            }
        data1 = {
            'name': "butter",
            'details': "second",
            'price': 199.88,
            'quantity': 3,
            'date_registration': "2023-10-24 12:42:31"
            }
        product = Product(**data)
        product.save()
        self.stdout.write(f'{product}')