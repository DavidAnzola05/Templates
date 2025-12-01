from rest_framework import serializers
from .models import vuelo
class VueloSerializer(serializers.ModelSerializer):
    class Meta:
        model = vuelo
        fields = '__all__'