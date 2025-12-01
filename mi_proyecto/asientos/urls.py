from django.urls import path
from .views import AsientoListCreateView, AsientoRetrieveUpdateDeleteView

urlpatterns = [
    path('', AsientoListCreateView.as_view(), name='asiento_list'),
    path('<int:pk>/', AsientoRetrieveUpdateDeleteView.as_view(), name='asiento_detail'),
]
