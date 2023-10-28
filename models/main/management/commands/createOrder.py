from django.core.management.base import BaseCommand
from main.models import Order, Client, Product, ProductSet
import random
import datetime

class Command(BaseCommand):
    help = "Create user."
    startDateTime = datetime.datetime(2023, 10, 28, 8, 0, 0)
    timeChange = datetime.timedelta(days=2)
    clientsLen = len(Client.objects.all())
    productsLen = len(Product.objects.all())


    def handle(self, *args, **kwargs):
        for diff in range(350):
            orderDateTime = self.startDateTime - datetime.timedelta(days=2*diff)
            idClient = random.randint(1, self.clientsLen)
            client = Client.objects.get(id=idClient)

            lenSetProducts = random.randint(1, 3)
            productSet = []
            totalCheck = 0
            for i in range(lenSetProducts):
                product = Product.objects.get(id=random.randint(1, self.productsLen))
                quant = random.randint(1, 10)
                productSet.append(ProductSet(product_id=product, quantity=quant))
                totalCheck += product.price * quant

            for el in productSet: el.save()

            data = {
                'client_id': client,
                'total_check': totalCheck,
                'date_order': orderDateTime,
            }
            order = Order(**data)
            order.save()
            for el in productSet: order.basket.add(el)