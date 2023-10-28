from django.core.management.base import BaseCommand
from main.models import Product
import random

class Command(BaseCommand):
    help = "Create user."
    shopProducts = {"thirst": "bread", "second": "butter", "third": "shugar", "fourth": "salt", "fifth": "potato",
                    "sixth": "tomato", "seventh": "chocolate", "eighth": "water",                
                    "ninth": "cookie", "tenth": "toothpaste", "eleventh": "tea"
                    }

    def handle(self, *args, **kwargs):
        dataAll = list(map(self.crateData, self.shopProducts.items()))
        for elm in dataAll:
            product = Product(**elm)
            product.save()
            self.stdout.write(f'{product}')

    def crateData(self, entry):
        data = {
            'name': entry[1],
            'details': entry[0],
            'price': round(random.uniform(1.33, 99.66), 2),
            'quantity': random.randint(5, 30),
            'date_registration': "2023-10-28 11:44:51"
            }
        return data