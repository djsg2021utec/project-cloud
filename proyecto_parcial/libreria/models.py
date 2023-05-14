from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.
#
class Almacen(models.Model):
    id = models.AutoField(primary_key=True)
    NombreProducto = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
    Unidades = models.IntegerField(null=True)
    Compra=models.FloatField(null=True)
    Venta=models.FloatField(null=True)

    def __str__(self):
        fila = "Nombre de Producto: "+ self.NombreProducto + "-" + "Marca: " + self.Marca + "-" + "Unidades: " + str(self.Unidades) + "-" + "Compra: " + str(self.Compra) + "-" + "Venta: " + str(self.Venta)
        return fila
    
    
class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    NombreCliente = models.CharField(max_length=100)
    ApellidoCliente = models.CharField(max_length=100)
    DNI = models.CharField(max_length=100)
    DireccionEntrega = models.CharField(max_length=100)
    Celular = models.CharField(max_length=100)
    NombreProducto = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
    Unidades = models.IntegerField(null=True)
    Precio=models.FloatField(null=True)

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    NombreProducto = models.CharField(max_length=100)
    Marca = models.CharField(max_length=100)
    Unidades = models.IntegerField(null=True)
    NombreCliente = models.CharField(max_length=100)
    ApellidoCliente = models.CharField(max_length=100)
    DNI = models.CharField(max_length=100)
    TotalVenta=models.FloatField(null=True)       
