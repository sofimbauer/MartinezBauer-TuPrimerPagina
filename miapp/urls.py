from django.urls import path
from miapp.views import inicio, clientes, registar_cliente

urlpatterns = [
    path('', inicio, name='inicio'),
    path('clientes/', clientes, name='clientes'),
    path('clientes/nuevo/', registar_cliente, name='registrar_cliente')
]
