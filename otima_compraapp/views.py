# C:\Users\Tali.b\PycharmProjects\otima_compra\otima_compraapp\views.py

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
