from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from .views.homepage_view import Homepage
from .views.hotels_view import Hotel_View
from .views.flights_view import Flight_View
from .views.cabs_view import Cab_View
from .views.detailed_hotel_view import Detailed_Hotel_View
from .views.cab_booking import Cab_Booking_View
from .views.flight_summary_view import Flight_Summary_View
<<<<<<< HEAD
from .views.hotel_summary_view import Hotel_Summary_View
=======
from .views.autocomplete import autocompleteModel
>>>>>>> 52b2a109166c84352f94f108586690b8e2293e1c

urlpatterns = [
    path('', Homepage, name="homepage"),
    path('hotels', Hotel_View.as_view(), name="hotels"),
    path('flights', Flight_View.as_view(), name="flights"),
    path('cabs', Cab_View.as_view(), name="cabs"),
    path('detailed_hotel', Detailed_Hotel_View.as_view(), name="detailed_hotel"),
    path('cab_booking', Cab_Booking_View.as_view(), name="cab_booking"),
    path('flight_summary', Flight_Summary_View.as_view(), name="flight_summary"),
<<<<<<< HEAD
    path('hotel_summary' , Hotel_Summary_View.as_view(), name = "hotel_summary"),
=======
    url(r'^ajax_calls/search/', autocompleteModel),
>>>>>>> 52b2a109166c84352f94f108586690b8e2293e1c
]
