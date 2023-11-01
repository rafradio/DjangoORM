from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.filter, name="index"),
    path('<int:pk>/<int:cl>/data', views.index, name="filter"),
    path('new_product', views.newProduct, name="product"),
]