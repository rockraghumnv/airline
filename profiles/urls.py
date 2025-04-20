from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'profile'

urlpatterns = [
    path('profile/', views.profile_view, name='profile_view'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('cancel_booking/', views.cancel_booking, name='cancel_booking'),]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)