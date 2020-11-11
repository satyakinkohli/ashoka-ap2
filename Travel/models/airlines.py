from django.db import models


class Airline(models.Model):
    name = models.CharField(max_length=50)
    logos = models.ImageField(upload_to = "uploads/airline_logos", null=True, default=None)

    def __str__(self):
        return self.name