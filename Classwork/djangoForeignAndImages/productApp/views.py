from django.shortcuts import render, redirect
from productApp.models import *
import os

# Create your views here.
def index(request):
    CategoryData = Category.objects.all()
    return render(request, "index.html", {'CategoryData': CategoryData})

def display(request):
    productData = Product.objects.all()
    return render(request, 'display.html', {'productData': productData})


def addProduct(request):
    data = request.POST
    productId = data.get('productId')
    productName = data.get('productName')
    productQty = data.get('productQty')
    productPrice = data.get('productPrice')
    category = data.get('productCategory')
    
    if productId: # UPDATE
        pobj = Product.objects.get(id=productId)
        pobj.productName = productName
        pobj.productQty = productQty
        pobj.productPrice = productPrice
        pobj.productCategory = Category.objects.get(id=category)
        if request.FILES.get('image'):  # remove previous image and add new one.
            os.remove("."+data.get('currImage'))
            pobj.productImage = request.FILES.get('image')
        pobj.save()

    else:   # ADD NEW 
        image = request.FILES.get('image')
        pobj = Product(
            productName=productName,
            productCategory = Category.objects.get(id=category),
            productQty = productQty,
            productPrice = productPrice,
            productImage = image,
        )
        pobj.save()
        # print('--->',productName, productQty, productPrice, category, image)

    return redirect('display') 


def deleteProduct(request):
    prodId = request.GET["prodId"]
    pobj = Product.objects.get(id=prodId)
    os.remove("."+pobj.productImage) # remove image from folder.
    pobj.delete()
    return redirect("display")

def updateProduct(request):
    prodId = request.GET["prodId"]
    pobj = Product.objects.get(id=prodId)
    CategoryData = Category.objects.all()
    return render(request, "index.html", {"prodObj": pobj, "CategoryData": CategoryData})