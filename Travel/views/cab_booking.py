from django.shortcuts import render
from django.views import View

from datetime import datetime, date
from Travel.models.cabs import Cab
from Travel.models.location import Location
from Travel.models.car_options import Car_options
from Travel.models.cab_driver import Cab_Driver


class Cab_Booking_View(View):
    def get(self, request):

        car_type = request.GET.get('car_type')
        car_type_id = Car_options.get_car_type(car_type)

        final_cars = Cab.get_car_through_type(car_type_id)

        cab_drivers = Cab_Driver.get_all_drivers()

        cab_from = request.session.get('cab_from')
        cab_to = request.session.get('cab_to')
        cab_date_formatted = request.session.get('cab_date_formatted')
        car_time = request.session.get('car_time')
       
        distance = request.session.get('cab_distance')

        cab_booking_data = {'cab_drivers': cab_drivers, 'final_cars': final_cars, 'car_type': car_type, 'cab_from': cab_from, 'cab_to': cab_to, 'distance': distance, 'cab_date_formatted': cab_date_formatted, 'car_time': car_time}

        return render(request, 'cab_list.html', cab_booking_data)