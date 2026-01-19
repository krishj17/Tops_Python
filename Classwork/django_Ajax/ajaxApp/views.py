from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ajaxApp.models import *

# Create your views here.
def index(request):
    return render(request, "index.html")

def country(request):
    countries = Country.objects.all()
    print(countries)
    return JsonResponse({"countries": list(countries.values())})


def state(request):
    countryId = request.GET['countryId']
    state = State.objects.filter(country_id=countryId)
    return JsonResponse({"states": list(state.values())})

def city(request):
    stateId = request.GET['stateId']
    city = City.objects.filter(state_id=stateId)
    return JsonResponse({"cities": list(city.values())})




# ---------------------------------------------------------------------
def register(request):
    data = request.GET['data']
    
    plist = Product.objects.filter(name__startswith=data)
    print(data, list(plist.values()))

    return JsonResponse({"products":list(plist.values())})