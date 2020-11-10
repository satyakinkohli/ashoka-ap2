from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50, default='Delhi')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    #vacancy = models.PositiveIntegerField(default=0)

        #if deluxe_room = True:
                #deluxe_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
                #deluxe_vacancy = models.PositiveIntegerField(default=0)

        #similarly for premium_room and suite_room


    @staticmethod
    def get_hotel_through_location(location):
        try:
            return Hotel.objects.get(location=location)
        except:
            return False