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
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT) 

    def __str__(self):
        return  self.nombre 

opciones_consulta= [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencias"], 
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    mensaje = models.TextField()
    tipo_consulta = models.IntegerField(choices= opciones_consulta)
    avisos = models.BooleanField()
    
    def __str__(self):
        return self.nombre