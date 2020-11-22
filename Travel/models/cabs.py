from django.db import models
from .car_options import Car_options

class Cab(models.Model):
	car = models.ForeignKey(Car_options, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, default="")
	number_plate = models.CharField(max_length=50, default="")
	air_conditioned = models.BooleanField(default=True)
	bluetooth_song = models.BooleanField(default=True)

	car_photo = models.ImageField(upload_to="uploads/cab_cars", null=True, default=None)

	@staticmethod
	def get_car_through_type(car):
		try:
			return Cab.objects.filter(car=car)
		except:
			return False