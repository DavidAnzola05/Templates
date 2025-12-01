from django.db import models

class Asiento(models.Model):
    TIPO_ASIENTO = [
        ('economico', 'Económico'),
        ('premium_economico', 'Premium Económico'),
        ('business', 'Business'),
        ('primera_clase', 'Primera Clase'),
    ]

    vuelo = models.ForeignKey('vuelo.Vuelo', on_delete=models.CASCADE)
    numero_asiento = models.CharField(max_length=5)
    tipo = models.CharField(max_length=20, choices=TIPO_ASIENTO)
    disponible = models.BooleanField(default=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)