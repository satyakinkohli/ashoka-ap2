from django.shortcuts import render
from django.views import View

import random

from datetime import datetime, date
from Travel.models.cabs import Cab
from Travel.models.location import Location
from Travel.models.car_options import Car_options


class Cab_View(View):
    def get(self, request):
        cab_from = request.GET.get('cab_from')
        cab_from_id = Location.get_location_through_name(cab_from)
        request.session['cab_from'] = cab_from

        cab_to = request.GET.get('cab_to')
        cab_to_id = Location.get_location_through_name(cab_to)
        request.session['cab_to'] = cab_to

        error_message = None
        if (cab_from_id == False or cab_to_id == False or ((cab_from_id) == (cab_to_id))):
            error_message = "Sorry, we do not have any available cabs as per your requirements!"

        cab_date = request.GET.get('cab_date')
        request.session['cab_date'] = cab_date

        # converting date to required format
        now = date(*map(int, cab_date.split('-')))
        
        cab_min_times = datetime.min.time()
        cab_date_adjust = datetime.combine(now, cab_min_times)

        cab_date_formatted = datetime.strftime(cab_date_adjust, "%A; %d %b. %Y")
        # end conversion
        request.session['cab_date_formatted'] = cab_date_formatted

        car_types = Car_options.get_all_car_types()
        distance = random.randint(50, 500)

        user = request.user
        if not request.user.is_authenticated:
            user_email = None
        else:
            user_email = user.email

        cab_data = {'user_email': user_email, 'cab_from': cab_from, 'cab_to': cab_to, 'cab_date': cab_date_formatted, 'error_message': error_message, 'car_types': car_types, 'distance': distance}

        return render(request, 'cab_service_choice.html', cab_data)

    def post(self, request):
        
        car_time = request.POST.get('car_time')
        request.session['car_time'] = car_time

        cab_from = request.session.get('cab_from')
        cab_to = request.session.get('cab_to')
        cab_date_formatted = request.session.get('cab_date_formatted')

        car_types = Car_options.get_all_car_types()

        distance = random.randint(50, 500)
        request.session['cab_distance'] = distance

        user = request.user
        if not request.user.is_authenticated:
            user_email = None
        else:
            user_email = user.email

        cab_data_post = {'user_email': user_email, 'cab_from': cab_from, 'cab_to': cab_to, 'cab_date': cab_date_formatted, 'car_time': car_time, 'car_types': car_types, 'distance': distance} 

        return render(request, 'cab_service_choice.html', cab_data_post)