from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VueloViewSet

router = DefaultRouter()
router.register(r'vuelo', VueloViewSet, basename='vuelo')

urlpatterns = [
    path('', include(router.urls)),
]