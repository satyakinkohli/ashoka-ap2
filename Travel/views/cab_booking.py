from django.shortcuts import render
from django.views import View

from datetime import datetime, date
from Travel.models.cabs import Cab
from Travel.models.location import Location
from Travel.models.car_options import Car_options


class Cab_Booking_View(View):
    def get(self, request):

        car_type = request.GET.get('car_type')
        print(car_type)

        cab_from = request.GET.get('cab_from')
        print(cab_from)

        cab_booking_data = {'car_type': car_type, 'cab_from': cab_from}

        return render(request, 'cab_list.html', cab_booking_data)