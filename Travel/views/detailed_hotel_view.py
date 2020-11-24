from django.shortcuts import render
from django.views import View

import random

from Travel.models.hotels import Hotel
from Travel.models.hotel_rating import Hotel_Rating


class Detailed_Hotel_View(View):
    def get(self, request):
        hotel_id = request.GET.get('hotel_id')
        request.session['hotel_id'] = hotel_id

        hotel_instance = Hotel.get_hotel_through_id(hotel_id)

        hotel_check_in = request.GET.get('hotel_check_in')
        hotel_check_out = request.GET.get('hotel_check_out')
        request.session['hotel_check_in'] = hotel_check_in
        request.session['hotel_check_out'] = hotel_check_out
        # print(hotel_check_in)
        # print(hotel_check_out)

        other_hotel_reviews = Hotel_Rating.get_review_through_hotel(
            hotel_instance)

        hotel_data = {'hotel': hotel_instance,
                      'hotel_check_in': hotel_check_in, 'hotel_check_out': hotel_check_out, 'other_hotel_reviews': other_hotel_reviews}

        return render(request, 'hotel_page.html', hotel_data)

    def post(self, request):
        hotel_review = request.POST.get('hotel_review')
        hotel_rating = request.POST.get('hotel_rating')
        hotel_id = request.session.get('hotel_id')
        hotel_instances_to_rate = Hotel.get_hotel_through_id(hotel_id)

        # reviewing hotel #
        rate = Hotel_Rating(
            hotel_name=hotel_instances_to_rate, review=hotel_review, rating=hotel_rating)
        rate.rate_hotel()
        # #

        hotel_check_in = request.session.get('hotel_check_in')
        hotel_check_out = request.session.get('hotel_check_out')

        other_hotel_reviews = Hotel_Rating.get_review_through_hotel(
            hotel_instance)

        hotel_data_post = {'hotel': hotel_instances_to_rate,
                           'hotel_check_in': hotel_check_in, 'hotel_check_out': hotel_check_out, 'other_hotel_reviews': other_hotel_reviews}

        return render(request, 'hotel_page.html', hotel_data_post)
