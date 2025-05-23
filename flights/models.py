from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.city} {self.code}'

class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='arrivals')
    duration = models.IntegerField()
    flight_name = models.CharField(max_length=50,default="NO FLIGHTS")

    def __str__(self):
        return f'{self.flight_name},{self.origin}, {self.destination}, {self.duration}'

class Passengers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=2)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    flights = models.ManyToManyField(Flights,blank=True,related_name='passengers')

    def __str__(self):
        return f'{self.first_name}_{self.last_name}'
