from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('profile/', views.profile_view, name='profile_view'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('bookings/', views.bookings_view, name='bookings_view'),
    path('cancel_booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]