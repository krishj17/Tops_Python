from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from myapp2.models import *
from myapp2.serializer import *
# Create your views here.

class Authors_Get_Post(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serialize = AuthorSerializer(authors, many=True)
        return Response({"authors": serialize.data})
    
    def post(self, request):
        serialize = AuthorSerializer(data=request.data)
        print(serialize)
        if serialize.is_valid():
            serialize.save()
            return Response({"status": "success", "data": serialize.data})
        else:
            return Response({"status": "error", "error": serialize.errors})
        
class Author_GetByID_Put_Delete(APIView):
    
    def get(self, request, id):
        author = Author.objects.get(id=id)
        serialize = AuthorSerializer(author)
        print(serialize)
        return Response({"status":"success", "data":serialize.data})
    
    def put(self, request, id):
        currData = Author.objects.get(id=id)
        serialize = AuthorSerializer(currData, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({"status": "success", "data": serialize.data})
        else:
            return Response({"status": "error", "error": serialize.errors})
        
    def delete(self, request, id):
        author = Author.objects.get(id=id)
        author.delete()
        return Response({"status": "success", "message": "author deleted successfully!"})
    

class Book_Get_Post(APIView):
    # GET all books in database
    def get(self, request):
        books = Book.objects.all()
        serialize = BookSerializer(books, many=True)
        return Response({"books":serialize.data})

    def post(self, request):
        serialize = BookSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({"status": "success", "data": serialize.data})
        else:
            return Response({"status": "error", "error": serialize.errors})


class Book_GetByID_Put_Delete(APIView):
    def get(self, request, id):
        books = Book.objects.get(id=id)
        serialize = BookSerializer(books)
        print(serialize)
        return Response({"status":"success", "data":serialize.data})
    
    def put(self, request, id):
        book = Book.objects.get(id=id)
        serialize = BookSerializer(book, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({"status":"success", "data":serialize.data})
        else: 
            return Response({"status": "error", "error": serialize.errors})
        
    def delete(self, request, id):
        book = Book.objects.get(id=id)
        book.delete()
        return Response({"status": "success", "message": "book deleted successfully!"})


