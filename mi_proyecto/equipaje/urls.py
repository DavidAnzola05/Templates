from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EquipajeViewSet

router = DefaultRouter()
router.register(r'equipaje', EquipajeViewSet, basename='equipaje')

urlpatterns = [
    path('', include(router.urls)),
]