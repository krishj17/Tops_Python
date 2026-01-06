from django.db import models

# Create your models here.
class Products(models.Model):
    productName = models.CharField(max_length=25,default="test",null=True)
    productCategory = models.CharField(max_length=20)
    productPrice = models.IntegerField()
