from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    address = models.CharField(max_length=300, blank=False, default='Moscow')
    date_registration = models.DateTimeField(blank=False, default=datetime.now)

    @classmethod
    def create(cls, name, email, phone_number, address, date_registration):
        client = cls(name=name, email=email, phone_number=phone_number, address=address, date_registration=date_registration)
        # do something with the book
        return client


    def __str__(self):
        return f'Name: {self.name}, phone_number: {self.phone_number}'
