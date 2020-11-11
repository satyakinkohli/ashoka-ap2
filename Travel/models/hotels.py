from django.db import models
from .location import Location


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
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

    @staticmethod
    def get_hotel_through_location(location):
        try:
            return Hotel.objects.get(location=location)
        except:
            return False
