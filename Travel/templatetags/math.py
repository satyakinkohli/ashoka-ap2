from django import template
from django.views import View

register = template.Library()


@register.filter(name='trip_price')
def trip_price(car_type_price, distance):
    return car_type_price * distance