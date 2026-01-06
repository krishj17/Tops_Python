from django.contrib import admin
from formApp.models import *

# Register your models here.

class StudentDisplay(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone", "age"]

admin.site.register(Student, StudentDisplay)