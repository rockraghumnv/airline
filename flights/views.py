from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import *
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request, 'flights/index.html',{'flights':Flights.objects.all()})

def flight(request,flight_id):
    try:
        flights = Flights.objects.get(id=flight_id)
        passengers = flights.passengers.all()
        non_passengers = Passengers.objects.exclude(flights=flights).all()
        
    except Flights.DoesNotExist:
            print("internal server error")
            return HttpResponse(f"No flights with id: {flight_id}")

    return render(request, 'flights/flight.html', {'flights':flights,
                                                    'passengers':passengers,
                                                   'non_passengers':non_passengers})

def book(request,flight_id):
     print("thd")
     if request.method == 'POST':
        try:
               passenger = Passengers.objects.get(pk=int(request.POST['passenger']))
               flight = Flights.objects.get(pk=flight_id)
        except KeyError:
               return HttpResponse("invalid Passenger")
        except Flights.DoesNotExist:
             return HttpResponse("FLights does not exist")
        except Passengers.DoesNotExist:
             return HttpResponse("Passengers deos not exist")
    
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('flights:flight',args=(flight_id,)))    

          
