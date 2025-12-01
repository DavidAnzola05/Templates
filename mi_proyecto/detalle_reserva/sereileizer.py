from rest_framework import serializers
from .models import detalle_reserva
class DetalleReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = detalle_reserva
        fields = '__all__'