from django.urls import path
from myapp.views import *

urlpatterns = [
    path('get', get_student),
    path('add', add_student),
    path('update/<id>', update_student),
    path('delete/<id>', delete_student),
]
