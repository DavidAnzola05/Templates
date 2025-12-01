from rest_framework import serializers
from .models import tripulacion
class TripulacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = tripulacion
        fields = '__all__'