from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AsignacionTripulacionViewSet

router = DefaultRouter()
router.register(r'', AsignacionTripulacionViewSet, basename='asignaciontripulacion')

urlpatterns = [
    path('', include(router.urls)),
]
