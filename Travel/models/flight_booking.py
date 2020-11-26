from django.db import models
from .flights import Flight
from .customers import Customer

class Flight_booking(models.Model):
    user_email = models.CharField(max_length=50, default='')
    user_fname = models.CharField(max_length=50, default='')
    user_lname = models.CharField(max_length=50, default='')
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    economy_number = models.PositiveIntegerField(default=0)
    business_number = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)




    @staticmethod
    def get_booking_by_user(email):        
        return Flight_booking.objects.filter(user_email=email)