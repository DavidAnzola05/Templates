from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import vuelo
from .sereileizer import VueloSerializer

# Create your views here.
class VueloViewSet(viewsets.ModelViewSet):
    queryset = vuelo.objects.all()
    serializer_class = VueloSerializer