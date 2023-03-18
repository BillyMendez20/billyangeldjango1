from django.urls import path
from .views import productos_por_categoria

urlpatterns = [
    path('productos_por_categoria/', productos_por_categoria, name='productos_por_categoria'),
]
