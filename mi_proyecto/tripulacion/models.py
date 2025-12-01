from django.db import models

# Create your models here.
class tripulacion(models.Model):
    tipo_tripulacion = [
        ('Piloto', 'Piloto'),
        ('Copiloto', 'Copiloto'),
        ('Auxiliar de Vuelo', 'Auxiliar de Vuelo'),
        ('Ingeniero de Vuelo', 'Ingeniero de Vuelo'),
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=tipo_tripulacion)
    aerolinea = models.ForeignKey('aerolinea.aerolinea', on_delete=models.CASCADE)
    licencia = models.CharField(max_length=50, unique=True)
    fecha_contratacion = models.DateField()
    