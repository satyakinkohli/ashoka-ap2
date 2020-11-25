from django.shortcuts import render
from django.views import View

from Travel.models.flights import Flight


class Flight_Summary_View(View):
    def get(self, request):
        economy_number = request.GET.get('economy')
        request.session['flight_economy_number'] = economy_number

        business_number = request.GET.get('business')
        request.session['flight_business_number'] = business_number

        flight_id = request.session.get('flight_id')
        request.session['flight_id'] = flight_id

        flight_instance = Flight.get_flight_through_id(flight_id)

        total_price = None
        error_message = None
        if flight_instance.economy_vacancy < int(economy_number) or flight_instance.business_vacancy < int(business_number):
            # error message
            error_message = "We do not have as many seats available."
            # reselect number of seats
        else:
            flight_instance.economy_vacancy -= int(economy_number)
            flight_instance.business_vacancy -= int(business_number)
            total_price = (int(economy_number)*float(flight_instance.economy_price)) + \
                (int(business_number)*float(flight_instance.business_price))

<<<<<<< HEAD
        print(total_price)
        user = request.user
        print(user)	
=======
>>>>>>> cc7cead4579e796840a7d94e954c84918af92646
        flight_instance.save()
        # flight_from = request.session.get('flight_from')
        # flight_from_id = request.session.get('flight_from_id')
        # flight_destination = request.session.get('flight_destination')
        # flight_destination_id = request.session.get('flight_destination_id')
        # flight_date = request.session.get('flight_date')

        flight_instance_usable = Flight.get_flight_through_id_but_queryset(
            flight_id)

        numbers_economy = list(range(1, int(economy_number) + 1))
        numbers_business = list(range(1, int(business_number) + 1))

        flight_summary_data = {'flight_instance': flight_instance, 'economy_number': economy_number, 'business_number': business_number, 'numbers_economy': numbers_economy, 'numbers_business': numbers_business,
                               'flight_instance_usable': flight_instance_usable, 'total_price': total_price, 'error_message': error_message}

        return render(request, 'flight_passenger_details.html', flight_summary_data)
