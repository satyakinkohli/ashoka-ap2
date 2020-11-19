from django.db import models

class Cab_Driver(models.Model):
    driver_name = models.CharField(max_length=50)
    driver_number = models.PositiveSmallIntegerField(default=9999999990)
    driver_rating = models.PositiveSmallIntegerField(default=5)
