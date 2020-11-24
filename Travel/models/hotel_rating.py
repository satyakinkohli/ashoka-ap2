from django.db import models
from .hotels import Hotel


class Hotel_Rating(models.Model):
    hotel_name = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    review = models.CharField(
        max_length=250, default="", null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5)

    def rate_hotel(self):
        self.save()

    def get_review_through_hotel(hotel_name):
        try:
            return Hotel_Rating.objects.filter(hotel_name=hotel_name)
        except:
            return None
