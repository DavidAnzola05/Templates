from django.db import models

class AsignacionTripulacion(models.Model):
    vuelo = models.ForeignKey('vuelo.Vuelo', on_delete=models.CASCADE)
    tripulante = models.ForeignKey('tripulacion.Tripulacion', on_delete=models.CASCADE)
    rol = models.CharField(max_length=100)
    turno = models.CharField(max_length=50)