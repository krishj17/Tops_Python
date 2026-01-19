from django.urls import path
from studentApp.views import *

urlpatterns = [
    path('', index, name="index"),
    path('addstudent', addstudent),
    path('getstudent', getstudent),
    path('deletestudent', deletestudent),
    path('loadStudent', loadStudent),
]
