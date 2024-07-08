# C:\Users\Tali.b\PycharmProjects\otima_compra\otima_compraapp\urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
