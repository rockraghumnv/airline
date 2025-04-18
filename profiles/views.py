from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from flights.models import Flights
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='users:login_redirect')
def profile_view(request):
    user = request.user  # Get the currently logged-in user
    flights = Flights.objects.filter(passengers__user=user)  # Retrieve flights associated with the user
    return render(request, 'profiles/profile.html', {
        'message': 'Profile View',
        'flights': flights
    })

def update_profile(request):
    return HttpResponse('Update Profile View will be updated soon')

def delete_profile(request):
    pass

def cancel_booking(request):
    return render(request, 'profiles/cancel_booking.html', {
        'message': 'Cancel Booking View will be updated soon'
    })