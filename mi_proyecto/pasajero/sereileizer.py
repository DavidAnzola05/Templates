from rest_framework import serializers
from .models import pasajero
class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = pasajero
        fields = '__all__'