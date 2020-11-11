from django.db import models
from .flights import Flight
from .customers import Customer

class Flight_booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    number_of_economy_tickets = models.PositiveIntegerField(default=0)
    number_of_business_tickets = models.PositiveIntegerField(default=0)
