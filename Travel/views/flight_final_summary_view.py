from django.shortcuts import render
from django.views import View

from Travel.models.flights import Flight


class Flight_Final_Summary_View(View):
    def get(self, request):
        economy_passenger_name_1 = request.GET.get('economy_passenger_name_1')
        print(economy_passenger_name_1)
        business_passenger_name_2 = request.GET.get(
            'business_passenger_name_2')
        print(business_passenger_name_2)
        return render(request, 'flight_final_summary.html')
