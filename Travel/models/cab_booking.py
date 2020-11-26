from django.db import models

class Cab_booking(models.Model):

    user_email = models.CharField(max_length=50, default='')
    user_fname = models.CharField(max_length=50, default='')
    user_lname = models.CharField(max_length=50, default='')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    source = models.CharField(max_length=50, default='')
    destination = models.CharField(max_length=50, default='')
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    car = models.CharField(max_length=50, default='')
    driver = models.CharField(max_length=50, default='')