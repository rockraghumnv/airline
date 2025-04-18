from django.shortcuts import render

# Create your views here.
def profile_view(request):
    return render(request, 'profiles/test.html',{'message': 'Profile View'})    

def update_profile(request):
    pass
def delete_profile(request):
    pass
def bookings_view(request):
    pass
def cancel_booking(request, booking_id):
    pass