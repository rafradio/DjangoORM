from django.db import models
from datetime import datetime
from .Product import Product

class ProductSet(models.Model):
    product_id =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity =  models.IntegerField()
    
    