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
        # flight_from = request.session.get('flight_from')
        # flight_from_id = request.session.get('flight_from_id')
        # flight_destination = request.session.get('flight_destination')
        # flight_destination_id = request.session.get('flight_destination_id')
        # flight_date = request.session.get('flight_date')

        flight_summary_data = {
            'flight_id': flight_id, 'economy_number': economy_number, 'business_number': business_number}

        return render(request, 'flight_final_summary.html', flight_summary_data)
