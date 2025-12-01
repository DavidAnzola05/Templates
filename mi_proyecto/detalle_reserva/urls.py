from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DetalleReservaViewSet

router = DefaultRouter()
router.register(r'detallereserva', DetalleReservaViewSet, basename='detallereserva')

urlpatterns = [
    path('', include(router.urls)),
]