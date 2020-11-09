from django.db import models

class Flight(models.Model):
	airline = models.CharField(max_length=50)
	source = models.CharField(max_length=50)
	destination = models.CharField(max_length=50)
	#departure_time = 
	#arrival time = 
	economy_vacancy = models.PositiveIntegerField(default=0)
	economy_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	business_vacancy = models.PositiveIntegerField(default=0)
	business_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	
