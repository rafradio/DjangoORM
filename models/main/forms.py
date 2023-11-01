from .models import Product
from django.forms import ModelForm

class NoteForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'details', 'price', 'quantity', 'date_registration']
