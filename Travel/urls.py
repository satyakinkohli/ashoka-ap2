from django.contrib import admin
from django.urls import path

from .views.homepage import Homepage

urlpatterns = [
    path('', Homepage, name="homepage"),
]
