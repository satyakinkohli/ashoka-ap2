from django.db import models
from .hotels import Hotel
from .customers import Customer
from .room_type import Room_type
from datetime import date

class Hotel_booking(models.Model):
    user_email = models.CharField(max_length=50, default='')
    user_fname = models.CharField(max_length=50, default='')
    user_lname = models.CharField(max_length=50, default='')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField(default = date.today)
    check_out_date = models.DateField(default = date.today)
    standard_number = models.PositiveIntegerField(default=0)
    deluxe_number = models.PositiveIntegerField(default=0)
    premium_number = models.PositiveIntegerField(default=0)
    suite_number = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)