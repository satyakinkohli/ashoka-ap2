from django.shortcuts import render
from django.views import View

from datetime import datetime, date

from Travel.models.flights import Flight

from Travel.models.flight_booking import Flight_booking


class Flight_Final_Summary_View(View):
    def get(self, request):
        economy_number = request.session.get('flight_economy_number')
        business_number = request.session.get('flight_business_number')
        
        economy_tickets = []
        for i in range(1, int(economy_number) + 1):
            economy_passenger_name = request.GET.get('economy_passenger_name_' + str(i))
            economy_passenger_gender = request.GET.get('economy_passenger_gender_' + str(i))
            economy_passenger_dob = request.GET.get('economy_passenger_dob_' + str(i))
            economy_passenger_phone = request.GET.get('economy_passenger_phone_' + str(i))
            # converting date to required format
            now = date(*map(int, economy_passenger_dob.split('-')))
            
            flight_min_time = datetime.min.time()
            economy_passenger_dob_adjust = datetime.combine(now, flight_min_time)

            economy_passenger_dob_formatted = datetime.strftime(economy_passenger_dob_adjust, "%d/%m/%y")
            # end conversion
            economy_tickets.append((economy_passenger_name, economy_passenger_gender, economy_passenger_dob_formatted, economy_passenger_phone, "Economy"))

        business_tickets = []
        for i in range(1, int(business_number) + 1):
            business_passenger_name = request.GET.get('business_passenger_name_' + str(i))
            business_passenger_gender = request.GET.get('business_passenger_gender_' + str(i))
            business_passenger_dob = request.GET.get('business_passenger_dob_' + str(i))
            business_passenger_phone = request.GET.get('business_passenger_phone_' + str(i))
            # converting date to required format
            now = date(*map(int, business_passenger_dob.split('-')))
            
            flight_min_time = datetime.min.time()
            business_passenger_dob_adjust = datetime.combine(now, flight_min_time)

            business_passenger_dob_formatted = datetime.strftime(business_passenger_dob_adjust, "%d/%m/%y")
            # end conversion
            business_tickets.append((business_passenger_name, business_passenger_gender, business_passenger_dob_formatted, business_passenger_phone, "Business"))
        
        flight_id = request.session.get('flight_id')
        flight_instance = Flight.get_flight_through_id(flight_id)
        flight_booked = Flight.get_flight_through_id_but_queryset(
            flight_id)

        flight_date = request.session.get('flight_date')
        # converting date to required format
        now = date(*map(int, flight_date.split('-')))

        total_price = (int(economy_number)*float(flight_instance.economy_price)) + \
                (int(business_number)*float(flight_instance.business_price))

        user = request.user
        flight_booking_instance = Flight_booking(user_email=user.email,
                                               user_fname=user.first_name,
                                               user_lname=user.last_name,
                                               flight=flight_instance,
                                               total_price=total_price,
                                               economy_number=int(
                                                   economy_number),
                                               business_number=int(
                                                   business_number))
        flight_booking_instance.save()
        
        flight_instance.economy_vacancy -= int(economy_number)
        flight_instance.business_vacancy -= int(business_number)
        flight_instance.save()

        flight_min_time = datetime.min.time()
        flight_date_adjust = datetime.combine(now, flight_min_time)

        flight_date_formatted = datetime.strftime(flight_date_adjust, "%A; %d %b. %Y")
        # end conversion

        flight_booking_data = {'total_price': total_price, 'flight_date_formatted': flight_date_formatted, 'flight_booked': flight_booked, 'economy_tickets': economy_tickets, 'business_tickets': business_tickets, 'economy_number': economy_number, 'business_number': business_number}

        return render(request, 'flight_final_summary.html', flight_booking_data)
