from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .form import Search_form
from django.http import JsonResponse

# Create your views here.

def flight_search(request,flight_id):
    if request.method == 'POST':    
        flights = Search_form(request.POST)
        if flights.is_valid():
             origin =flights.cleaned_data["origin"]
             destination = flights.cleaned_data["destination"]

             request.session["origin"] = origin
             request.session["destination"] = destination

        try:
            flights_list = Flights.objects.filter(origin=origin,destination=destination).values()
            return render(request,'flights/flight_list.html',{'flights':flights_list})
            
        except Flights.DoesNotExist:
                print("internal server error")
                return HttpResponse(f"No flights with id: {flight_id}")

    return render(request,'flights/flight_search.html',{'Search_form':Search_form})

@login_required('/login_redirect')
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

def success(request):
     pass
          
def suggestions(request):
     if request.method == "GET":
          query = request.GET.get('q')
          dropdown_list = Flights.objects.filter(city__startswith = query).values_list('flight_name',flat=True).distinct() 
          if dropdown_list:
               return JsonResponse({'results':list(dropdown_list)})
        

def login_redirect(request,flight_id):
     request.session["flight_id"] = flight_id
     if request.user.is_authenticated:
          return redirect("flights:book_flight",flight_id=flight_id)
     return redirect("/login")

def login(request):
     pass