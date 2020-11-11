from django.db import models
from .hotels import Hotel
from .customers import Customer
from .room_type import Room_type
from datetime import date

class Hotel_booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField(default = date.today)
    check_out_date = models.DateField(default = date.today)
    room_type = models.ForeignKey(Room_type, on_delete=models.CASCADE, default=1)