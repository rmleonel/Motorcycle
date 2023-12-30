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

def formulario(request):
    
    if request.method == "POST":

        marca = request.POST.get("marca")
        modelo = request.POST.get("modelo")
        año = request.POST.get("año")

        moto_luxury = Luxury(marca=marca, modelo=modelo, año=año)
        moto_luxury.save()

        moto_medium = Medium(marca=marca, modelo=modelo, año=año)
        moto_medium.save()

        moto_economy = Economy(marca=marca, modelo=modelo, año=año)
        moto_economy.save()
        return render(request,'index.html')

    return render(request, "formulario.html")