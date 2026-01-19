from django.contrib import admin
from studentApp.models import *

# Register your models here.

class studentDisplay(admin.ModelAdmin):
    list_display = ("id", "sName", "sAge", "sPhone")


admin.site.register(Student, studentDisplay)