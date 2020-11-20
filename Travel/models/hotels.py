from django.db import models
from .location import Location


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    number = models.PositiveSmallIntegerField(default=9999999900)
    website = models.URLField(default="www..com", max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

    deluxe_available = models.BooleanField(default=True)
    deluxe_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    standard_available = models.BooleanField(default=True)
    standard_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    premium_available = models.BooleanField(default=True)
    premium_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    suite_available = models.BooleanField(default=True)
    suite_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    #boolean facilities
    wifi = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=True)
    airport_shuttle = models.BooleanField(default=False)
    parking_area = models.BooleanField(default=True)
    pool = models.BooleanField(default=False)
    fitness_center = models.BooleanField(default=False)


    @staticmethod
    def get_correct_hotel_through_location(location):
        try:
            return Hotel.objects.filter(location=location)
        except:
            return False


    @staticmethod
    def get_hotel_through_id(ids):
        try:
            return Hotel.objects.get(id=ids)
        except:
            return False
