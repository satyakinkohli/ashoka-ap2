from django.contrib import admin
from django.urls import path

from .views.homepage import Homepage
from .views.flights_view import Flight_View

urlpatterns = [
    path('', Homepage, name="homepage"),
    path('flights', Flight_View, name="flights"),
]
