from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()


class Employee(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    salary = models.FloatField()
