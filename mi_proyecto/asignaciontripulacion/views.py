from rest_framework import viewsets
from .models import AsignacionTripulacion
from .sereileizer import AsignacionTripulacionSerializer

class AsignacionTripulacionViewSet(viewsets.ModelViewSet):
    queryset = AsignacionTripulacion.objects.all()
    serializer_class = AsignacionTripulacionSerializer
