from django.db import models
from .hotels import Hotel
from .customers import Customer

class Hotel_booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    #check_in_date = 
    #check_out_date =
    #room_type = 