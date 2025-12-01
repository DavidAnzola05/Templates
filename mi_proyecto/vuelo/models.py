from django.db import models

# Create your models here.
class vuelo(models.Model):
    estado_vuelo=[
        ('programado','Programado'),
        ('enbarcado','Enbarcado'),
        ('en_vuelo','En Vuelo'),
        ('aterrizado','Aterrizado'),
        ('cancelado','Cancelado'),
     ]
    aerolinea=models.ForeignKey('aerolinea.aerolinea',on_delete=models.CASCADE) 
    numero_vuelo=models.CharField(max_length=10)
    aeropuerto_salida=models.ForeignKey('aeropuerto.aeropuerto',related_name='vuelos_salida',on_delete=models.CASCADE)
    aeropuerto_llegada=models.ForeignKey('aeropuerto.aeropuerto',related_name='vuelos_llegada',on_delete=models.CASCADE)
    fecha_salida=models.DateTimeField()
    fecha_llegada=models.DateTimeField()
    estado=models.CharField(max_length=20,choices=estado_vuelo,default='programado')
    duracion_estimada=models.DurationField()
    distancia=models.IntegerField(help_text='Distancia en kilómetros')  