from django.shortcuts import render
from django.views import View

import random

from datetime import datetime, date
from Travel.models.cabs import Cab
from Travel.models.location import Location
from Travel.models.car_options import Car_options
from Travel.models.cab_driver import Cab_Driver
from Travel.models.cab_booking import Cab_booking


class Cab_Booking_View(View):
    def get(self, request):

        car_type = request.GET.get('car_type')
        car_type_id = Car_options.get_car_type(car_type)
        distance = request.session.get('cab_distance')

        #
        final_cars_id = Cab.objects.filter(car=car_type_id).values_list('id', flat=True)
        final_cars_id_list = random.sample(list(final_cars_id), min(len(final_cars_id), 1))
        final_cars = Cab.objects.filter(id__in=final_cars_id_list)
        for cab in final_cars:
            car = cab.name
            car_type_price = cab.car.price * distance
        print(car)
        print (car_type_price)
        
        #
        cab_drivers_id = Cab_Driver.objects.filter().values_list('id', flat=True)
        cab_drivers_id_list = random.sample(list(cab_drivers_id), min(len(cab_drivers_id), 1))
        cab_drivers = Cab_Driver.objects.filter(id__in=cab_drivers_id_list)
        for drivers in cab_drivers:
            driver = drivers.driver_name
        print (driver)
                    #

        cab_from = request.session.get('cab_from')
        cab_to = request.session.get('cab_to')
        cab_date_formatted = request.session.get('cab_date_formatted')
        cab_date = request.session.get('cab_date')
        cab_date_1 = datetime.strptime(cab_date, '%Y-%m-%d')


        car_time = request.session.get('car_time')
       
        distance = request.session.get('cab_distance')

        user = request.user
        cab_booking_instance = Cab_booking(user_email=user.email,
                                               user_fname=user.first_name,
                                               user_lname=user.last_name,
                                               booking_date= cab_date_1,
                                               total_price=car_type_price,
                                               booking_time= car_time,
                                               source= cab_from,
                                               destination = cab_to,
                                               car = car,
                                               driver = driver)
        cab_booking_instance.save()

        #
        cab_booking_data = {'cab_drivers': cab_drivers, 'final_cars': final_cars, 'car_type': car_type, 'cab_from': cab_from, 'cab_to': cab_to, 'distance': distance, 'cab_date_formatted': cab_date_formatted, 'car_time': car_time}
        #
        
        return render(request, 'cab_list.html', cab_booking_data)