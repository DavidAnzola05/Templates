from rest_framework import serializers
from .models import equipaje
class EquipajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = equipaje
        fields = '__all__'