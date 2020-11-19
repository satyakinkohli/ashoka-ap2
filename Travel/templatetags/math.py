from django import template
from django.views import View

import random

register = template.Library()


@register.filter(name='trip_price')
def trip_price(car_type_price):
    distance = random.randint(50, 500)
    print(distance)
    return car_type_price * distance