from django.urls import path
from .views import home, contacto, somos, registro, shop, agregar_producto, listar_productos

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('registro/', registro, name="registro"),
    path('somos/', somos, name="somos"),
    path('shop/', shop, name="shop"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
]