from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @staticmethod
    def get_location_through_name(name):
        try:
            location = Location.objects.get(name=name)
            return location.id
        except:
            return False