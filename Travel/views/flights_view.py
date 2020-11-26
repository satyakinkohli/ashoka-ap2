from django.shortcuts import render
from django.views import View

from Travel.models.flights import Flight
from Travel.models.location import Location


class Flight_View(View):
    def get(self, request):
        categoryID = request.GET.get('lth')

        if not categoryID:

            flight_from = request.GET.get('flight_from')
            flight_from_id = Location.get_location_through_name(flight_from)
            request.session['flight_from'] = flight_from
            request.session['flight_from_id'] = flight_from_id

            flight_destination = request.GET.get('flight_destination')
            flight_destination_id = Location.get_location_through_name(
            flight_destination)
            request.session['flight_destination'] = flight_destination
            request.session['flight_destination_id'] = flight_destination_id

            flight_date = request.GET.get('flight_date')
            request.session['flight_date'] = flight_date

        else:
            flight_from_id = request.session.get('flight_from_id')        
            flight_destination_id = request.session.get('flight_destination_id')        
            flight_date = request.session.get('flight_date')

        

        if categoryID:
            print(flight_from_id)
            possible_flights = Flight.get_correct_flight_through_location_and_date_ordered(
            flight_from_id, flight_destination_id, flight_date)
            print (possible_flights)
        else:
            print(flight_from_id)
            possible_flights = Flight.get_correct_flight_through_location_and_date(
            flight_from_id, flight_destination_id, flight_date)

        

        error_message = None
        if len(possible_flights) == 0:
            error_message = "Sorry, we do not have any available flights as per your requirements!"

        user = request.user
        if not request.user.is_authenticated:
            user_email = None
        else:
            user_email = user.email

        flight_data = {'possible_flights': possible_flights,
                       'error_message': error_message, 'user_email': user_email}

        return render(request, 'flight_list.html', flight_data)

    def post(self, request):
        flight_id = request.POST.get('flight_id')
        request.session['flight_id'] = flight_id

        flight_from = request.session.get('flight_from')
        flight_from_id = request.session.get('flight_from_id')
        flight_destination = request.session.get('flight_destination')
        flight_destination_id = request.session.get('flight_destination_id')
        flight_date = request.session.get('flight_date')

        possible_flights = Flight.get_correct_flight_through_location_and_date(
            flight_from_id, flight_destination_id, flight_date)

        user = request.user
        if not request.user.is_authenticated:
            user_email = None
        else:
            user_email = user.email

        flight_data_post = {'user_email': user_email, 
            'possible_flights': possible_flights, 'flight_id': flight_id}

        return render(request, "flight_list.html", flight_data_post)
