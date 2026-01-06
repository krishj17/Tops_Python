from django.urls import path
from company.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('display', display, name='display'),

    path('addDepart', addDepart, name="addDepart"),
    path('updateDepart', updateDepart, name="updateDepart"),
    path('removeDepart', removeDepart, name="removeDepart"),

    path('addEmp', addEmp, name="addEmp"),
    path('updateEmp', updateEmp, name='updateEmp'),
    path('deleteEmp', deleteEmp, name='deleteEmp'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
