from django.shortcuts import render
from django.views import View

from Travel.models.flights import Flight


class Flight_Summary_View(View):
    def get(self, request):
        return render(request, 'flight_final_summary.html')
