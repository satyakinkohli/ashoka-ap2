from django.shortcuts import render
from django.views import View
from datetime import datetime
from Travel.models.hotels import Hotel


class Hotel_Summary_View(View):
    def get(self, request):
        hotel_id = request.GET.get('hotel_id')
        # print(hotel_id)
        hotel_instance = Hotel.get_hotel_through_id(hotel_id)

        hotel_check_in = request.GET.get('hotel_check_in')
        hotel_check_out = request.GET.get('hotel_check_out')
        print(hotel_check_in)
        print(hotel_check_out)
        hotel_check_in_1 = datetime.strptime(hotel_check_in, '%Y-%m-%d')
        hotel_check_out_1 = datetime.strptime(hotel_check_out, '%Y-%m-%d')
        days = hotel_check_out_1 - hotel_check_in_1

        standard_number = request.GET.get('standard')
        # print(standard_number)
        deluxe_number = request.GET.get('deluxe')
        # print(deluxe_number)
        premium_number = request.GET.get('premium')
        # print(premium_number)
        suite_number = request.GET.get('suite')
        # print(suite_number)

        price_per_night = (int(standard_number)*float(hotel_instance.standard_price)) + (int(deluxe_number)*float(hotel_instance.deluxe_price)
                                                                                         ) + (int(premium_number)*float(hotel_instance.premium_price)) + (int(suite_number)*float(hotel_instance.suite_price))
        print(price_per_night)
        total_price = price_per_night*int(days.days)
        print(total_price)
        summary_data = {'hotel': hotel_instance, 'hotel_check_in': hotel_check_in, 'hotel_check_out': hotel_check_out,
                        'days': days.days, 'price_per_night': price_per_night, 'total_price': total_price}
        return render(request, "hotel_final_summary.html", summary_data)
