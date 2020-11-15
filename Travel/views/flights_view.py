from django.shortcuts import render
from django.views import View

from Travel.models.flights import Flight


class Flight_View(View):
    def get(self, request):
        flight_from = request.GET.get('flight_from')
        locations = {'Delhi':1 , 'Mumbai':2 , 'Bangalore':3 , 'Pune':4 , 'Kolkata':5 , 'Jaipur':6}
        from_id=(locations[flight_from])

        #print(flight_from)
        flight_destination = request.GET.get('flight_destination')
        #print(flight_destination)

        destination_id=(locations[flight_destination])
        possible_flights = Flight.get_correct_flight(from_id,destination_id)
        print (possible_flights)

        data = {'possible_flights': possible_flights}
        
        return render(request, 'flight_list.html', data)


# def Flight_View(request):
#     return render(request, 'flight_list.html')


