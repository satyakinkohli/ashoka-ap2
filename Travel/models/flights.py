from django.db import models
import datetime
from datetime import date
from .location import Location
from .airlines import Airline

class Flight(models.Model):
<<<<<<< HEAD
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, default=1)
    source = models.ForeignKey(Location, related_name="source", on_delete=models.CASCADE, default=1)
    destination = models.ForeignKey(Location, related_name="destination", on_delete=models.CASCADE, default=1)
    date = models.DateField(default = date.today)
    departure_time = models.TimeField(default=datetime.datetime.now())
    arrival_time = models.TimeField(default=datetime.datetime.now())
=======
    airline = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    #departure_time = 
    #arrival_time = 
>>>>>>> df772f075c5718e201d39f69e2e818adffeb3c28
    economy_vacancy = models.PositiveIntegerField(default=0)
    economy_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    business_vacancy = models.PositiveIntegerField(default=0)
    business_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)



    @staticmethod
    def get_flight_through_source(source):
        try:
            return Flight.objects.get(source=source)
        except:
            return False

    @staticmethod
    def get_flight_through_destination(destination):
        try:
            return Flight.objects.get(destination=destination)
        except:
            return False
    
