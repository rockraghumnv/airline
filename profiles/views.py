from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from flights.models import Flights
from django.http import HttpResponse
from .models import UserProfile,cancelled
from .forms import CancelForm

# Create your views here.
@login_required(login_url='users:login_redirect')
def profile_view(request):
    user = request.user  # Get the currently logged-in user
    flights = Flights.objects.filter(passengers__user=user)  # Retrieve flights associated with the user
    return render(request, 'profiles/profile.html', {
        'message': 'Profile View',
        'flights': flights,
        'UserProfile': UserProfile.objects.get(user=user),
    })

def update_profile(request):
    return HttpResponse('Update Profile View will be updated soon')

def delete_profile(request):
    pass

@login_required(login_url='users:login_redirect')
def cancel_booking(request):
    if request.method == 'POST':
        form = CancelForm(request.POST)
        if form.is_valid():
            # Process the cancellation form
            reason = form.cleaned_data['reason']
            flight_id = request.POST.get('flight_id')
            if flight_id and reason:
                # Check if a cancellation record already exists for the user
                if not cancelled.objects.filter(user=request.user).exists():
                    cancelled.objects.create(
                        user=request.user,
                        reason=reason
                    )
                else:
                    return render(request, 'profiles/cancel_booking.html', {
                        'message': 'You have already cancelled a booking.',
                        'form': CancelForm(),
                    })
                flight = Flights.objects.get(id=flight_id)
                request.user.flights.remove(flight)
                flight.passengers.remove(request.user)
                flight.save()   
                return render(request, 'profiles/cancel_booking.html', {
                    'flight_id': flight_id,
                    'message': 'Booking cancelled successfully!',
                })
        else:
            flight_cancel_id = request.POST.get('flight_cancel_id')
            if flight_cancel_id:
                request.session['cancel_booking'] = flight_cancel_id
                flight = Flights.objects.get(id=flight_cancel_id)  
                return render(request, 'profiles/cancel_booking.html', {
                    'form': CancelForm(),
                    'flights': flight,
                })
    # Fallback response to ensure HttpResponse is always returned
    return render(request, 'profiles/cancel_booking.html', {
        'message': 'Invalid request or missing data.',
        'form': CancelForm(),
    })