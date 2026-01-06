from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    phone = models.CharField(max_length=12)
    age = models.IntegerField()
    