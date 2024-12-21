from django.db import models

# Create your models here.

class Airport(models.Model):
    city = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.city} {self.code}'

class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='departures')
    destnation = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='arrivals')
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.origin}, {self.destnation}, {self.duration}'

class Passengers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=20)
    flights = models.ManyToManyField(Flights,blank=True,related_name='passengers')

    def __str__(self):
        return f'{self.first_name}_{self.last_name}'
