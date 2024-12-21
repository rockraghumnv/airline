from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'flights/index.html',{'flights':Flights.objects.all()})

def flight(request,flight_id):
    try:
        flights = Flights.objects.get(id=flight_id)
        passengers = flights.passengers.all()
 
    except Flights.DoesNotExist:
            print("internal server error")
            return HttpResponse(f"No flights with id: {flight_id}")

    return render(request, 'flights/flight.html', {'flights':flights,'passengers':passengers})

