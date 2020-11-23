from django.shortcuts import render
from django.views import View

from Travel.models.flights import Flight

class Flight_Summary_View(View):
    def post(self, request):
    	economy_number = request.POST.get('economy')
    	print(economy_number)
    	business_number = request.POST.get('business')
    	print(business_number)
    	flight_id = request.POST.get('flight_id')
    	print(flight_id)
    	return render (request, "base1.html")