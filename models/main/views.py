from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, Product
import datetime

def index(request, pk, cl):
    print(f'Наш клиент {cl}')
    startDateTime = datetime.datetime.now()
    timeDiff = datetime.timedelta(days=pk)
    ordersDateTime = startDateTime - timeDiff
    orders = Order.objects.filter(date_order__gte=ordersDateTime).filter(client_id=cl)
    notes = []
    data = {'orders': orders}
    return render(request, 'main/index.html', data)

def filter(request):
    return render(request, 'main/about.html')

def newProduct(request):
    if request.method == 'POST':
        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            'name': request.POST['title'],
            'details': request.POST['body'],
            'price': request.POST['price'],
            'quantity': request.POST['quantity'],
            'date_registration': d,
            # 'date_registration': request.POST['date'],
        }
        product = Product(**data)
        product.save()
        print(f'Данные из формы {data["name"]} {data["price"]}')

    return render(request, 'main/product.html')

