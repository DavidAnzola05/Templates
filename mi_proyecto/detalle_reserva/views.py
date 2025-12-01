from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import detalle_reserva
from .sereileizer import DetalleReservaSerializer
# Create your views here.
class DetalleReservaViewSet(viewsets.ModelViewSet):
    queryset = detalle_reserva.objects.all()
    serializer_class = DetalleReservaSerializer