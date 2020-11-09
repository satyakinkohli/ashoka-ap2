from django.contrib import admin

from .models.hotels import Hotel
from .models.flights import Flight
from .models.customers import Customer
from .models.flight_booking import Flight_booking
from .models.hotel_booking import Hotel_booking

admin.site.register(Hotel)
admin.site.register(Flight)
admin.site.register(Customer)
admin.site.register(Flight_booking)
admin.site.register(Hotel_booking)



