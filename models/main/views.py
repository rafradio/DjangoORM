from django.shortcuts import render
from django.http import HttpResponse
from .models import Order
import datetime

def index(request):
    startDateTime = datetime.datetime.now()
    timeDiff = datetime.timedelta(days=7)
    ordersDateTime = startDateTime - timeDiff
    orders = Order.objects.filter(date_order__gte=ordersDateTime)
    notes = []
    data = {'orders': orders}
    return render(request, 'main/index.html', data)

def filter(request):
    return render(request, 'main/about.html')

