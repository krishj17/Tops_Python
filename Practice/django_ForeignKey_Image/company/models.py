from django.db import models

# Create your models here.
class Department(models.Model):
    departName = models.CharField(max_length=15)
    def __str__(self):
        return self.departName
    
class Employee(models.Model):
    empName = models.CharField(max_length=15)
    empImage = models.ImageField(upload_to='images')
    empDepart = models.ForeignKey(Department, on_delete=models.CASCADE)
    empAge = models.IntegerField()
    empSalary = models.FloatField()
