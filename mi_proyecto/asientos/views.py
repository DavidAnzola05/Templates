from rest_framework import generics
from .models import Asiento
from .serializers import AsientoSerializer

class AsientoListCreateView(generics.ListCreateAPIView):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer

class AsientoRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asiento.objects.all()
    serializer_class = AsientoSerializer
