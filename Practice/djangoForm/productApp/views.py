from django.shortcuts import render, redirect
from productApp.models import *

# Create your views here.

def productForm(request):
    return render(request ,"productForm.html")


def productDisplay(request):
    productData = Products.objects.all()
    return render(request, "productDisplay.html", {"productData": productData})


def addProduct(request):
    productData = request.POST
    id = productData.get('id')
    name = productData.get("name")
    category = productData.get("category")
    price = productData.get("price")
    print(id, name, category, price)

    if id:
        product = Products.objects.get(id=id)
        product.productName=name
        product.productCategory=category
        product.productPrice=price
        product.save()
        return render(request, "productForm.html", {"message": "Product Updated Successfully!!"})
    else:
        product = Products(productName=name,productCategory=category, productPrice=price)
        product.save()
        return render(request, "productForm.html", {"message": "Product Added Successfully!!"})


def deleteProduct(request):
    productId = request.GET['productId']
    print("product to be deleted: ", productId)
    product = Products.objects.get(id=productId)
    product.delete()
    return redirect("productDisplay")


def updateProduct(request):
    productId = request.GET['productId']
    print("Product to be updated id: ", productId)
    productData = Products.objects.get(id=productId)
    return render(request, "productForm.html", {'productData': productData})