from django.contrib import admin
from productApp.models import *

# Register your models here.
class ProductDisplay(admin.ModelAdmin):
    list_display = ['id', 'productName', 'productCategory', 'productQty', 'productPrice', 'productImage']

class CategoryDisplay(admin.ModelAdmin):
    list_display = ['id', 'CategoryName']

admin.site.register(Product, ProductDisplay)
admin.site.register(Category, CategoryDisplay)