from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, Product
import datetime
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

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
        f = request.FILES['fileToUpload']
        data = {
            'name': request.POST['title'],
            'details': request.POST['body'],
            'price': request.POST['price'],
            'quantity': request.POST['quantity'],
            'date_registration': d,
            'image': f.name
            # 'date_registration': request.POST['date'],
        }
        filename = 'media/'+ f.name
        # path = default_storage.save(filename, ContentFile(f.read()))
        with open(filename, "wb+") as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        product = Product(**data)
        product.save()
        print(f'Данные из формы {data["name"]} {data["price"]}')
        print(f'Файл {type(f)} {f.content_type} {f.size}')

    return render(request, 'main/product.html')

