from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=15)


class Country(models.Model):
    countryName = models.CharField(max_length=25)
    def __str__(self):
        return self.countryName
    
class State(models.Model):
    stateName = models.CharField(max_length=25)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.stateName
    
class City(models.Model):
    cityName = models.CharField(max_length=25)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return self.cityName
    

