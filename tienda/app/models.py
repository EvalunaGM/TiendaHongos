from django.db import models

# Create your models here.
class Proveedor (models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self):
        return  self.nombre

class Producto (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField(max_length=100)
    imagen = models.ImageField(upload_to="productos", null=True)
    stock = models.IntegerField(default=0)
    proovedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT) 

    def __str__(self):
        return  self.nombre 