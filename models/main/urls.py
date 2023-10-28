from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.filter, name="index"),
    path('<int:pk>/data', views.index, name="filter"),
]