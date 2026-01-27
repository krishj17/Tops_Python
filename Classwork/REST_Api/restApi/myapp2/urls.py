from django.urls import path
from myapp2.views import *

urlpatterns = [
    path("authors", Authors_Get_Post.as_view()), # for GET and POST
    path("authors/<id>", Author_GetByID_Put_Delete.as_view()), # for PUT and DELETE

    path("books", Book_Get_Post.as_view()),
    path("books/<id>", Book_GetByID_Put_Delete.as_view()),
]
