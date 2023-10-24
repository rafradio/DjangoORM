from django.db import models
from datetime import datetime

class Newnote(models.Model):
    title = models.CharField( max_length=45, default='Название')
    body = models.TextField()
    date = models.DateTimeField(blank=False, default=datetime.now)

    def __str__(self):
        return f'Name: {self.title}'