from django.db import models


class Car_options(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    capacity = models.PositiveSmallIntegerField(default=4)
    type_options = models.ImageField(upload_to = "uploads/cab_types", null=True, default=None)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_car_types():
        return Car_options.objects.all()
