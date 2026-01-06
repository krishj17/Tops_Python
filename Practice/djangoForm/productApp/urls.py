from django.urls import path
from productApp.views import *

urlpatterns = [
    path("", productForm, name="productForm"),
    path("productDisplay", productDisplay, name="productDisplay"),
    path("addProduct", addProduct, name="addProduct"),
    path("deleteProduct", deleteProduct, name="deleteProduct"),
    path("updateProduct", updateProduct, name="updateProduct"),
]
