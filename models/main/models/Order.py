from django.db import models
from datetime import datetime
from .Client import Client
from .Product import Product

class Order(models.Model):
    client_id =  models.ForeignKey(Client, on_delete=models.CASCADE)
    basket = models.ManyToManyField(Product)
    total_check = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateTimeField(blank=False, default=datetime.now)

    def __str__(self):
        return f'Name: {self.id}, price: {self.total_check}'
