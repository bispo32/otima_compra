# C:\Users\Tali.b\PycharmProjects\otima_compra\otima_compra\urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('otima_compraapp/', include('otima_compraapp.urls')),
]
