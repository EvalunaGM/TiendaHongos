from django import forms
from django.forms import fields
from .models import Contacto, Producto, Proveedor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'correo', 'mensaje', 'tipo_consulta', 'avisos']

class CustomUserCreationForm(UserCreationForm):
    pass

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion', 'imagen', 'stock', 'proveedor']

        