from django.db import models

# Create your models here.
class pasajero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    pasaporte = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)