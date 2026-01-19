from django.urls import path
from ajaxApp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("country", country, name="country"),
    path("state", state, name="state"),
    path("city", city, name="city"),


    # path("register", register, name="register")

]
