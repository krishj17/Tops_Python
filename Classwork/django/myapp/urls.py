from django.urls import path
from myapp.views import *
urlpatterns = [
    path("", index, name="index"),      # here name method is used to set the name which is used in layout.html in url section.
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("help/", help, name="help"),
]