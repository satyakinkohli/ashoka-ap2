from django.shortcuts import render
from django.views import View

import time
import datetime
import random

from Travel.models.cab_booking import Cab_booking
from Travel.models.hotel_booking import Hotel_booking
from Travel.models.flight_booking import Flight_booking
from Travel.models.location import Location
from Travel.models.hotels import Hotel
from Travel.models.flights import Flight

# def Homepage(request):
#     return render(request, 'homepage.html')

class Homepage_View(View):
    def get(self, request):

        user = request.user
        if not request.user.is_authenticated:
            user_email = None
        else:
            user_email = user.email
        
        recent_date_1 = datetime.date(1, 1, 1) 
        recent_date_2 = datetime.date(1, 1, 1) 
        recent_date_3 = datetime.date(1, 1, 1) 

        hotel_bookings = Hotel_booking.get_ordered_booking_by_user(user_email)
        if hotel_bookings:
            recent_hotel = hotel_bookings[0].hotel.location
            recent_date_1 = hotel_bookings[0].check_out_date
        
        flight_bookings = Flight_booking.get_ordered_booking_by_user(user_email)
        if flight_bookings:
            recent_flight = flight_bookings[0].flight.destination
            recent_date_2 = flight_bookings[0].flight.date

        cab_bookings = Cab_booking.get_ordered_booking_by_user(user_email)
        if cab_bookings:
            recent_cab = cab_bookings[0].destination
            recent_date_3 = cab_bookings[0].booking_date

        if recent_date_1 > recent_date_2:
            recent_date = recent_date_1
        else:
            recent_date = recent_date_2

        if recent_date > recent_date_3:
            pass
        else:
            recent_date = recent_date_3

        if recent_date == recent_date_1:
            recent_destination = recent_hotel
        if recent_date == recent_date_2:
            recent_destination = recent_flight
        if recent_date == recent_date_3:
            recent_destination = recent_cab

        recent_destination_id = Location.get_location_through_name(recent_destination)

        personal_hotels_id = Hotel.objects.filter(location=recent_destination_id).values_list('id', flat=True)
        personal_hotels_id_list = random.sample(list(personal_hotels_id), min(len(personal_hotels_id), 4))
        personal_hotels = Hotel.objects.filter(id__in=personal_hotels_id_list)

        personal_flights_id = Flight.objects.filter(source=recent_destination_id, date=recent_date).values_list('id', flat=True)
        personal_flights_id_list = random.sample(list(personal_flights_id), min(len(personal_flights_id), 4))
        personal_flights = Flight.objects.filter(id__in=personal_flights_id_list)

        personal_recommendations = {'personal_hotels': personal_hotels, 'personal_flights': personal_flights, 'recent_destination': recent_destination}

        return render(request, 'homepage.html', personal_recommendations)