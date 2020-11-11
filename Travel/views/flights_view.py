from django.shortcuts import render
from django.views import View


# class Flight_View(View):
#     def get(self, request):
#         # categoryID = request.GET.get('category')
#         return render(request, 'flight_list.html')


def Flight_View(request):
    return render(request, 'flight_list.html')
