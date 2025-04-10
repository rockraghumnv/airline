from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .form import Search_form,Book_form
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
            flights_list = Flights.objects.filter(origin=origin, destination=destination)
            if not flights_list.exists():
                    return render(request, 'flights/flight_list.html', {'message': 'No flights found'})
            
            return render(request,'flights/flight_list.html',{'flights':flights_list})
            
        except Flights.DoesNotExist:
                print("internal server error")
                return HttpResponse(f"No flights with id: {flight_id}")

    return render(request,'flights/flight_search.html',{'Search_form':Search_form})


@login_required(login_url='users:login_view')
def book(request,flight_id):
     if request.method == 'POST':
        form = Book_form(request.POST)

        if form.is_valid():
            firstname =  form.cleaned_data["firstname"]    
            lastname = form.cleaned_data["lastname"]   

        else:
               return render(request,'flights/book.html',{"message":"invalid"})


        try:
               flight = Flights.objects.get(pk=flight_id)
               book = Passengers(user=request.user,first_name=firstname,last_name=lastname)
               book.save()
               book.flights.add(flight)
               return render(request,'flights/success.html',{"message":'booking success'})

        except KeyError:
               return HttpResponse("invalid Passenger")
        except Flights.DoesNotExist:
             return HttpResponse("FLights does not exist")
        except Passengers.DoesNotExist:
             return HttpResponse("Passengers deos not exist")  

     return render(request,'flights/book.html',{"flight_id":flight_id,'register_form':Book_form})

def suggestions(request):
     if request.method == "GET":
          query = request.GET.get('q')
          dropdown_list = Flights.objects.filter(flight_name__istartswith=query).values_list('flight_name', flat=True).distinct()
          if dropdown_list:
               return JsonResponse({'results':list(dropdown_list)})
        
