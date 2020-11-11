from django.db import models
from .flights import Flight
from .customers import Customer

class Flight_booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    #number_of_tickets = 
    #ticket_type = 
