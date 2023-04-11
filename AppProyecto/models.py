from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    DNI=models.CharField(max_length=8)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Proveedor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    CUIT=models.CharField(max_length=13)
    email=models.EmailField()
    condicion_pago=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Producto(models.Model):
    descripcion=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    unidad_de_medida=models.CharField(max_length=50,default="")
    precio=models.FloatField()
    def __str__(self):
        return f"Descripción: {self.descripcion} - Marca: {self.marca} - Precio: {self.precio}"