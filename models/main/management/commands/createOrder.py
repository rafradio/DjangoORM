from django.core.management.base import BaseCommand
from main.models import Order, Client, Product, ProductSet

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        idClient = 1
        idProduct1 = 1
        idProduct2 = 2
        client = Client.objects.get(id=idClient)
        product1 = Product.objects.get(id=idProduct1)
        product2 = Product.objects.get(id=idProduct2)
        productSet = [ProductSet(product_id=product1, quantity=3), ProductSet(product_id=product2, quantity=4)]
        for el in productSet: el.save()
        data = {
            'client_id': client,
            'total_check': 500.5,
            'date_order': "2023-10-24 12:00:51",
            # 'basket': [product1, product2]
            }
        order = Order(**data)
        order.save()
        for el in productSet: order.basket.add(el)
        # order.basket.add(productSet[0])
        # order.basket.add(productSet[1])
        self.stdout.write(f'{order}')