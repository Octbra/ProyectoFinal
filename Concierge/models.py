from django.db import models

# Create your models here.
class Restaurantes(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=150)
    tipo_cocina=models.CharField(max_length=50)
    numero_telefono=models.IntegerField()
    
class Bares(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=150)
    tipo_bar=models.CharField(max_length=50)
    numero_telefono=models.IntegerField()
    
class Clientes(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    es_huesped=models.BooleanField()
    habitacion=models.IntegerField()
    numero_telefono=models.IntegerField()