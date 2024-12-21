from django.contrib import admin
from .models import *
# Register your models here.

class Flightadmin(admin.ModelAdmin):
    list_display = ['id','origin','destnation','duration']

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ('flights',)


admin.site.register(Flights,Flightadmin)
admin.site.register(Airport)
admin.site.register(Passengers,PassengerAdmin)
