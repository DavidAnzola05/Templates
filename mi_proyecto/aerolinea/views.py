from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import aerolinea
from .sereileizer import aerolineaSerializer

class aerolinealistcreate(generics.ListCreateAPIView):
    queryset = aerolinea.objects.all()
    serializer_class = aerolineaSerializer

class aerolineaupdatedelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = aerolinea.objects.all()
    serializer_class = aerolineaSerializer

class aerolineaViewSet(viewsets.ModelViewSet):
    queryset = aerolinea.objects.all()
    serializer_class = aerolineaSerializer
