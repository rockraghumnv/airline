from django.shortcuts import render,HttpResponse
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .form import Search_form,Book_form
from django.http import JsonResponse

# Create your views here.

def flight_search(request):
    if request.method == 'POST':    
        flights = Search_form(request.POST)
        if flights.is_valid():
            origin = flights.cleaned_data["origin"]
            destination = flights.cleaned_data["destination"]


            # Extract the ID part from the concatenated string (e.g., 'china,2')
            try:
                origin_id = int(origin.split(',')[-1])
                destination_id = int(destination.split(',')[-1])
            except (ValueError, IndexError):
                return render(request, 'flights/flight_list.html', {'message': 'Invalid origin or destination format'})

            request.session["origin"] = origin_id
            request.session["destination"] = destination_id

            try:
                flights_list = Flights.objects.filter(origin=origin_id, destination=destination_id)
                if not flights_list.exists():
                    return render(request, 'flights/flight_list.html', {'message': 'No flights found'})

                return render(request, 'flights/flight_list.html', {'flights': flights_list})

            except Flights.DoesNotExist:
                print("internal server error")
                return HttpResponse(f"No flights")

    return render(request, 'flights/flight_search.html', {'Search_form': Search_form()})


@login_required(login_url='users:login_view')
def book(request):

     if request.method == 'POST':
        form = Book_form(request.POST)

        if form.is_valid():
            firstname =  form.cleaned_data["firstname"]    
            lastname = form.cleaned_data["lastname"]

        else:
           flight_id = request.POST.get('flight_id')
           flight = Flights.objects.get(pk=flight_id)
           return render(request,'flights/book.html',{"flight":flight,'register_form':Book_form})

        if Passengers.objects.filter(user=request.user, flights=flight).exists():
            return render(request, 'flights/success.html', {"message": "You have already booked this flight."})


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


def suggestions(request):
     if request.method == "GET":
          print("sdjnl")
          query = request.GET.get('q')
          dropdown_list = Airport.objects.filter(city__istartswith=query).values_list('city','id').distinct()
          print(dropdown_list)
          if dropdown_list:
               return JsonResponse({'results':list(dropdown_list)})
        
          return JsonResponse({'results': list(dropdown_list)})
