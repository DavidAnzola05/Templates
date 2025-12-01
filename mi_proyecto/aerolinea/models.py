from django.db import models

# Create your models here.
class aerolinea(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    pais_origen = models.CharField(max_length=100)
    fecha_fundacion = models.DateField()
    sitio_web = models.URLField()
    telefono_contacto = models.CharField(max_length=15)
   