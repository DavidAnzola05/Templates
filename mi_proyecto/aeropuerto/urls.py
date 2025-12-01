from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AeropuertoViewSet

router = DefaultRouter()
router.register(r'aeropuerto', AeropuertoViewSet, basename='aeropuerto')

urlpatterns = [
    path('', include(router.urls)),
]