from rest_framework import serializers
from .models import aerolinea
class aerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = aerolinea
        fields = '__all__'