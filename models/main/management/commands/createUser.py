from django.core.management.base import BaseCommand
from main.models import Client
from main.models import Newnote

class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        client = Client(name="Beethoven", email="ludvig@gmail.com", phone_number="+19155674321", address="Moscow")
        client.date_registration = "2023-10-25 12:00:51"
        # client = Client.create("Mozart", "amad@mail.ru", "+79155674321", "Moscow", "2023-10-23")
        client.save()
        self.stdout.write(f'{client}')
        