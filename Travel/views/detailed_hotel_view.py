from django.shortcuts import render
from django.views import View

from Travel.models.hotels import Hotel

class Detailed_Hotel_View(View):
    def get(self,request):
        hotel_id = request.GET.get('hotel_id')
        hotel_instance = Hotel.get_hotel_through_id(hotel_id)
        print (hotel_instance)

        hotel_check_in = request.GET.get('hotel_check_in')
        hotel_check_out = request.GET.get('hotel_check_out')
        #print(hotel_check_in)
        #print(hotel_check_out)

        hotel_data = {'hotel': hotel_instance, 'hotel_check_in': hotel_check_in, 'hotel_check_out': hotel_check_out}
        return render(request , 'hotel_page.html' , hotel_data)
