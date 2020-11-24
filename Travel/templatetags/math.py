from django import template
from django.views import View

from Travel.models.hotel_rating import Hotel_Rating

register = template.Library()


@register.filter(name='trip_price')
def trip_price(car_type_price, distance):
    return car_type_price * distance


@register.filter(name='ratings')
def ratings(hotel_id):
    serial = Hotel_Rating.get_review_through_hotel(hotel_id)
    total_ratings = len(serial)

    if total_ratings == 0:
        total_ratings = 1
    else:
        pass

    opinion = 0
    for item in serial:
        opinion += item.rating

    rated = round((opinion / total_ratings), 2)
    if rated == 0:
        rated = "-"
    else:
        pass

    return rated
