from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import tripulacion
from .sereileizer import TripulacionSerializer
# Create your views here.
class TripulacionViewSet(viewsets.ModelViewSet):
    queryset = tripulacion.objects.all()
    serializer_class = TripulacionSerializer
    