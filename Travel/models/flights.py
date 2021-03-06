from django.db import models
import datetime
from datetime import date
from .location import Location
from .airlines import Airline


class Flight(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, default=1)
    source = models.ForeignKey(
        Location, related_name="source", on_delete=models.CASCADE, default=1)
    destination = models.ForeignKey(
        Location, related_name="destination", on_delete=models.CASCADE, default=1)
    date = models.DateField(default=date.today)
    departure_time = models.TimeField(default=datetime.datetime.now())
    arrival_time = models.TimeField(default=datetime.datetime.now())
    economy_vacancy = models.PositiveIntegerField(default=0)
    economy_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    business_vacancy = models.PositiveIntegerField(default=0)
    business_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)

    # @staticmethod
    # def get_flight_through_source(source):
    #     try:
    #         return Flight.objects.get(source=source)
    #     except:
    #         return False

    # @staticmethod
    # def get_flight_through_destination(destination):
    #     try:
    #         return Flight.objects.get(destination=destination)
    #     except:
    #         return False

    @staticmethod
    def get_correct_flight_through_location_and_date(source, destination, date):
        try:
            return Flight.objects.filter(source=source, destination=destination, date=date)
        except:
            return False


    @staticmethod
    def get_correct_flight_through_location_and_date_ordered(source, destination, date):
        try:
            return Flight.objects.filter(source=source, destination=destination, date=date).order_by('economy_price')
        except:
            return False


    @staticmethod
    def get_correct_flight_through_location_and_date_reversed(source, destination, date):
        try:
            return Flight.objects.filter(source=source, destination=destination, date=date).order_by('-economy_price')
        except:
            return False


    @staticmethod
    def get_correct_flight_through_location_and_date_earliest(source, destination, date):
        try:
            return Flight.objects.filter(source=source, destination=destination, date=date).order_by('departure_time')
        except:
            return False


    @staticmethod
    def get_correct_flight_through_location_and_date_latest(source, destination, date):
        try:
            return Flight.objects.filter(source=source, destination=destination, date=date).order_by('-departure_time')
        except:
            return False

    @staticmethod
    def get_correct_flight_through_source_and_date(source, date):
        try:
            return Flight.objects.filter(source=source, date=date)
        except:
            return False

    @staticmethod
    def get_flight_through_id(ids):
        try:
            return Flight.objects.get(id=ids)
        except:
            return False

    @staticmethod
    def get_flight_through_id_but_queryset(ids):
        try:
            return Flight.objects.filter(id=ids)
        except:
            return False
