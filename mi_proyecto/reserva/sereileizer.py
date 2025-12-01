from rest_framework import serializers
from .models import reserva
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = reserva
        fields = '__all__'