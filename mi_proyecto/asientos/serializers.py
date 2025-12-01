from rest_framework import serializers
from .models import Asiento

class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asiento
        fields = '__all__'
