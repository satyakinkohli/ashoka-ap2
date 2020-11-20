from django.contrib import admin
from django.urls import path

from .views.homepage_view import Homepage
from .views.hotels_view import Hotel_View
from .views.flights_view import Flight_View
from .views.cabs_view import Cab_View
from .views.detailed_hotel_view import Detailed_Hotel_View

urlpatterns = [
    path('', Homepage, name="homepage"),
    path('hotels', Hotel_View.as_view(), name="hotels"),
    path('flights', Flight_View.as_view(), name="flights"),
    path('cabs', Cab_View.as_view(), name="cabs"),
    path('detailed_hotel', Detailed_Hotel_View.as_view(), name="detailed_hotel")
]
