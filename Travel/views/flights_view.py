from django.shortcuts import render
from django.views import View

from Travel.models.flights import Flight
from Travel.models.location import Location


class Flight_View(View):
    def get(self, request):
        flight_from = request.GET.get('flight_from')
        flight_from_id = Location.get_location_through_name(flight_from)
        
        flight_destination = request.GET.get('flight_destination')
        flight_destination_id = Location.get_location_through_name(flight_destination)
        
        flight_date = request.GET.get('flight_date')
        
        possible_flights = Flight.get_correct_flight_through_location_and_date(flight_from_id, flight_destination_id, flight_date)

        error_message = None
        if len(possible_flights) == 0:
            error_message = "Sorry, we do not have any available flights as per your requirements!"
        
        data = {'possible_flights': possible_flights, 'error_message': error_message}
        
        return render(request, 'flight_list.html', data)
