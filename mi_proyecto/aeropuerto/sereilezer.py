from rest_framework import serializers
from .models import aeropuerto

class aeropuertoSerializer(serializers.ModelSerializer):
    class Meta:
        model = aeropuerto
        fields = '__all__'
