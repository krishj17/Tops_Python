from django.db import models

# Create your models here.
class Category(models.Model):
    CategoryName = models.CharField(max_length=20)

    def __str__(self):
        return self.CategoryName
    

class Product(models.Model):
    productName = models.CharField(max_length=20)
    productCategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    productQty = models.IntegerField()
    productPrice = models.IntegerField()
    productImage = models.ImageField(upload_to='images')
