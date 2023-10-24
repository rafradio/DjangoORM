from django.db import models
from datetime import datetime

class Product(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity =  models.IntegerField()
    date_registration = models.DateTimeField(blank=False, default=datetime.now)

    def __str__(self):
        return f'Name: {self.name}, price: {self.price}'
    