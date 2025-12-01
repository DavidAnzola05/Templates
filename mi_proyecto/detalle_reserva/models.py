from django.db import models

# Create your models here.
class detalle_reserva(models.Model):
    reserva = models.ForeignKey('reserva.reserva', on_delete=models.CASCADE)
    vuelo = models.ForeignKey('vuelo.vuelo', on_delete=models.CASCADE)
    asiento = models.ForeignKey('asientos.asiento', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    clase = models.CharField(max_length=50)