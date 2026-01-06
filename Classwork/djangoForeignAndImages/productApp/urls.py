from django.urls import path, include
from productApp.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('display', display, name='display'),
    path('addproduct', addProduct, name='addproduct'),
    path('deleteProduct', deleteProduct, name="deleteProduct"),
    path('updateProduct', updateProduct, name="updateProduct")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
