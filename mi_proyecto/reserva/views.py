from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import reserva
from .sereileizer import ReservaSerializer
# Create your views here.
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = reserva.objects.all()
    serializer_class = ReservaSerializer    