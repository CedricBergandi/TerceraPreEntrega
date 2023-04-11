from django.urls import path
from .views import *

urlpatterns = [
    path('',inicioApp,name="inicioApp"),
    path('clientes/',clientes,name="clientes"),
    path('proveedores/',proveedores,name="proveedores"),
    path('productos/',productos,name="productos"),
    path('busqueda_marca/',busqueda_marca,name="busqueda_marca"),
    path('buscar/',buscar,name="buscar"),

]