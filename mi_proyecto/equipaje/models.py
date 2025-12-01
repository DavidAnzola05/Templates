from django.db import models

# Create your models here.
class equipaje(models.Model):
    reserva = models.ForeignKey('reserva.reserva', on_delete=models.CASCADE)
    numero_pieza = models.IntegerField()
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2)
    tipo=models.CharField(max_length=50,choices=[
        ('equipaje_mano','Equipaje de Mano'),
        ('bodega','Equipaje de Bodega'),
    ])
    costo_extra=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)