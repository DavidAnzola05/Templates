from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import pasajero
from .sereileizer import PasajeroSerializer
# Create your views here.
class PasajeroViewSet(viewsets.ModelViewSet):
    queryset = pasajero.objects.all()
    serializer_class = PasajeroSerializer