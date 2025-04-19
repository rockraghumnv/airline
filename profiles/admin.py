from django.contrib import admin
from .models import UserProfile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date','phone_number', 'location','photo')
    search_fields = ('user__username', 'location')
    list_filter = ('birth_date',)
    
admin.site.register(UserProfile, ProfileAdmin)  