from django.shortcuts import render
from django.views import View

from Travel.models.hotels import Hotel
from Travel.models.location import Location


class Hotel_View(View):
    def get(self, request):
        hotel_where = request.GET.get('hotel_where')
        hotel_where_id = Location.get_location_through_name(hotel_where)

        hotel_check_in = request.GET.get('hotel_check_in')
        hotel_check_out = request.GET.get('hotel_check_out')
        
        possible_hotels = Hotel.get_correct_hotel_through_location(hotel_where_id)

        error_message = None
        if len(possible_hotels) == 0:
            error_message = "Sorry, we do not have any available hotels as per your requirements!"
        
        data = {'possible_hotels': possible_hotels, 'error_message': error_message}
        
        return render(request, 'hotel_list.html', data)
