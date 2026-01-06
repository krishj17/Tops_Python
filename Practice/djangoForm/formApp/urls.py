from django.urls import path
from formApp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("register", register, name="register"),
    path("display", display, name="display"),
    path("delete", deleteData, name="delete"),
    path("update", updateData, name="update")
]

