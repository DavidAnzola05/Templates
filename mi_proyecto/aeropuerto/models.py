from django.db import models

# Create your models here.
class aeropuerto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=3, unique=True)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    terminales = models.IntegerField()
    capacidad_pasajeros = models.IntegerField()