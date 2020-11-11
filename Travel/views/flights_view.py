from django.shortcuts import render
from django.views import View

from Travel.models.flights import Flight


class Flight_View(View):
    def get(self, request):
        flight_from = request.GET.get('flight_from')
        print(flight_from)
        flight_destination = request.session.get('flight_destination')
        print(flight_destination)

        possible_flights = Flight.get_correct_flight(flight_from, flight_destination)

        data = {'possible_flights': possible_flights}
        
        return render(request, 'flight_list.html', data)


# def Flight_View(request):
#     return render(request, 'flight_list.html')
