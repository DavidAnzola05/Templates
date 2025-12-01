from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import aeropuerto
from .sereilezer import aeropuertoSerializer

class aeropuertolistcreate(generics.ListCreateAPIView):
    queryset = aeropuerto.objects.all()
    serializer_class = aeropuertoSerializer

class aeropuertoupdatedelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = aeropuerto.objects.all()
    serializer_class = aeropuertoSerializer

class AeropuertoViewSet(viewsets.ModelViewSet):
    queryset = aeropuerto.objects.all()
    serializer_class = aeropuertoSerializer
