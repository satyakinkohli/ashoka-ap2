from django.shortcuts import render
from django.views import View

from Travel.models.flights import Flight


class Flight_Summary_View(View):
    def get(self, request):
        economy_number = request.GET.get('economy')
        print(economy_number)
        request.session['flight_economy_number'] = economy_number

        business_number = request.GET.get('business')
        print(business_number)
        request.session['flight_business_number'] = business_number

        flight_id = request.session.get('flight_id')
        print(flight_id)
        flight_instance = Flight.get_flight_through_id(flight_id)

        print (flight_instance.economy_vacancy)
        error_message = None

        if flight_instance.economy_vacancy < int(economy_number) or flight_instance.business_vacancy < int(business_number):
        	#error message
        	error_message = "We do not have as many seats available."
        	#reselect number of seats
        else:
        	flight_instance.economy_vacancy -= int(economy_number)
        	flight_instance.business_vacancy -= int(business_number)
        	total_price = (int(economy_number)*float(flight_instance.economy_price)) + (int(business_number)*float(flight_instance.business_price)
                                                                                         )

        print(total_price)	
        flight_instance.save()
        # flight_from = request.session.get('flight_from')
        # flight_from_id = request.session.get('flight_from_id')
        # flight_destination = request.session.get('flight_destination')
        # flight_destination_id = request.session.get('flight_destination_id')
        # flight_date = request.session.get('flight_date')

        flight_summary_data = {
            'flight': flight_instance, 'economy_number': economy_number, 'business_number': business_number, 'total_price':total_price,'error_message':error_message}

        return render(request, 'flight_final_summary.html', flight_summary_data)
