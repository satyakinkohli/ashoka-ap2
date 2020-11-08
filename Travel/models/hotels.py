from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    gh = jh