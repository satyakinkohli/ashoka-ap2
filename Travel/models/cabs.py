from django.db import models
from .car_options import Car_options

class Cab(models.Model):
	car = models.ForeignKey(Car_options, on_delete=models.CASCADE)
	air_conditioned = models.BooleanField(default=True)
	car_photo = models.ImageField(upload_to = "uploads/cab_cars", null=True, default=None)
