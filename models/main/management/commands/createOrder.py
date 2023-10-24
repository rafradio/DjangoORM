from django.core.management.base import BaseCommand
from main.models import Order, Client, Product

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        idClient = 1
        idProduct1 = 1
        idProduct2 = 2
        client = Client.objects.get(id=idClient)
        product1 = Product.objects.get(id=idProduct1)
        product2 = Product.objects.get(id=idProduct2)
        products = [product1, product2]
        data = {
            'client_id': client,
            'total_check': 500.5,
            'date_order': "2023-10-24 12:00:51",
            # 'basket': [product1, product2]
            }
        order = Order(**data)
        order.save()
        order.basket.add(product1)
        order.basket.add(product2)
        # order.save()
        self.stdout.write(f'{order}')