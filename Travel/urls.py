from django.contrib import admin
from django.urls import path

from .views.homepage_view import Homepage
from .views.flights_view import Flight_View

urlpatterns = [
    path('', Homepage, name="homepage"),
    path('flights', Flight_View.as_view(), name="flights"),
]
