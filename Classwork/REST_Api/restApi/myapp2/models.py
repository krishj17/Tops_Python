from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)

class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    qty = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)    