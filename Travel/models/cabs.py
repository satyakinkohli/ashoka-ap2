from django.db import models
from .car_options import Car_options

class Cab(models.Model):
	car = models.ForeignKey(Car_options, on_delete=models.CASCADE)
	air_conditioned = models.BooleanField(default=True)
	capacity = models.PositiveIntegerField(default=0)
	price = models.DecimalField(max_digits=6, decimal_places=2, default=0)