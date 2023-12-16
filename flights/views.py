from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def flight(request, flight_id):
    fli = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": fli,
        "passengers": fli.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=fli).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        fli = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(fli)
        return HttpResponseRedirect(reverse("flight", args=(fli.id, )))

