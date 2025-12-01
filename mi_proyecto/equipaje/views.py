from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import equipaje
from .sereileizer import EquipajeSerializer
# Create your views here.
class EquipajeViewSet(viewsets.ModelViewSet):
    queryset = equipaje.objects.all()
    serializer_class = EquipajeSerializer