from django.contrib import admin
from productApp.models import *
# Register your models here.

class ProductDisplay(admin.ModelAdmin):
    list_display = ["productName", "productCategory", "productPrice"]

admin.site.register(Products, ProductDisplay)