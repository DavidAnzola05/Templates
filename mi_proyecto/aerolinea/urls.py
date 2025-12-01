from rest_framework import viewsets
from .models import aerolinea
from .sereileizer import aerolineaSerializer

class aerolineaViewSet(viewsets.ModelViewSet):
    queryset = aerolinea.objects.all()
    serializer_class = aerolineaSerializer
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import aerolineaViewSet

router = DefaultRouter()
router.register(r'aerolinea', aerolineaViewSet, basename='aerolinea')

urlpatterns = [
    path('', include(router.urls)),
]
