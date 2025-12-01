"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('aerolinea/', include('aerolinea.urls')),
    path('aeropuerto/', include('aeropuerto.urls')),
    path('vuelo/', include('vuelo.urls')),
    path('asientos/', include('asientos.urls')),
    path('tripulacion/', include('tripulacion.urls')),
    path('asignaciontripulacion/', include('asignaciontripulacion.urls')),
    path('pasajero/', include('pasajero.urls')),
    path('reserva/', include('reserva.urls')),
    path('detalle_reserva/', include('detalle_reserva.urls')),
    path('equipaje/', include('equipaje.urls')),
]
