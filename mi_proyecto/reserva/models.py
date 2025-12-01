from django.db import models

# Create your models here.
class reserva(models.Model):
    estado_reserva=[
        ('pendiente','Pendiente'),
        ('confirmada','Confirmada'),
        ('cancelada','Cancelada'),
        ('check_in','Check-in Realizado'),
        ]
    codigo_reserva=models.CharField(max_length=20, unique=True)
    pasajero=models.ForeignKey('pasajero.pasajero',on_delete=models.CASCADE)
    fecha_reserva=models.DateTimeField(auto_now_add=True)
    estado=models.CharField(max_length=20,choices=estado_reserva,default='pendiente')
    total=models.DecimalField(max_digits=10,decimal_places=2)
    