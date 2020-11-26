from django.contrib import admin

from .models.hotels import Hotel
from .models.flights import Flight
from .models.customers import Customer
from .models.flight_booking import Flight_booking
from .models.hotel_booking import Hotel_booking
from .models.location import Location
from .models.room_type import Room_type
from .models.airlines import Airline
from .models.cabs import Cab
from .models.car_options import Car_options
from .models.cab_driver import Cab_Driver
from .models.hotel_rating import Hotel_Rating
from .models.cab_booking import Cab_booking


admin.site.register(Hotel)
admin.site.register(Flight)
admin.site.register(Customer)
admin.site.register(Flight_booking)
admin.site.register(Hotel_booking)
admin.site.register(Location)
admin.site.register(Room_type)
admin.site.register(Airline)
admin.site.register(Cab)
admin.site.register(Car_options)
admin.site.register(Cab_Driver)
admin.site.register(Hotel_Rating)
admin.site.register(Cab_booking)