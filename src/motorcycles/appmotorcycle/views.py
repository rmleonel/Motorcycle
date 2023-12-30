from django.shortcuts import render
from django.http import HttpResponse
from appmotorcycle.models import Luxury, Medium, Economy

def index(request):
    return render (request, "index.html")

def luxury(request):
    return render(request, 'luxury.html')

def medium(request):
    return render(request, 'medium.html')

def economy(request):
    return render(request, 'economy.html')
