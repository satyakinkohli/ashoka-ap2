from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout as auth_logout


def Logout(request):
    auth_logout(request)
    return redirect('/')