from django.contrib import admin
from company.models import *

# Register your models here.

class EmployeeDisplay(admin.ModelAdmin):
    list_display = ['id', 'empName', 'empDepart', 'empAge', 'empSalary', 'empImage']

class DepartmentDisplay(admin.ModelAdmin):
    list_display = ['id', 'departName']


admin.site.register(Employee, EmployeeDisplay)
admin.site.register(Department, DepartmentDisplay)
