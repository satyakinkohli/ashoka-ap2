from django.shortcuts import render
from django.views import View
from Travel.models.cab_booking import Cab_booking
from Travel.models.hotel_booking import Hotel_booking
from Travel.models.flight_booking import Flight_booking

class My_bookings_view(View):
    def get(self, request):
        user = request.user
        
        hotel_bookings = Hotel_booking.get_booking_by_user(user.email)
        print(hotel_bookings)

        flight_bookings = Flight_booking.get_booking_by_user(user.email)
        print(flight_bookings)

        cab_bookings = Cab_booking.get_booking_by_user(user.email)
        print(cab_bookings)

        return render(request , 'my_bookings.html',{'hotel_bookings':hotel_bookings, 'flight_bookings':flight_bookings,'cab_bookings':cab_bookings})