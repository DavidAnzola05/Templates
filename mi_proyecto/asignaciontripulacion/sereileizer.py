from rest_framework import serializers
from .models import AsignacionTripulacion

class AsignacionTripulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionTripulacion
        fields = '__all__'
