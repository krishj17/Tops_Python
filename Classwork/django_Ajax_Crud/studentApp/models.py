from django.db import models

# Create your models here.

class Student(models.Model):
    sName = models.CharField(max_length=20, default="default0")
    sAge = models.IntegerField(default=0)
    sPhone = models.IntegerField(default=0)