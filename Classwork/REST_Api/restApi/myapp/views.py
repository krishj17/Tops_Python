from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.serialize import *
from myapp.models import *

# Create your views here.

@api_view(["GET"])
def get_student(request):
    data = Student.objects.all()
    serialized_data = student_Serialize(data, many=True)
    return Response({"student data":serialized_data.data})

@api_view(["POST"])
def add_student(request):
    new_data = request.data
    serialize_and_add = student_Serialize(data=new_data)
    if serialize_and_add.is_valid():
        serialize_and_add.save()
        return Response({"message": "Student added successfully!", "data":serialize_and_add.data})
    else:
        return Response({"message":"Error while adding!", "errors":serialize_and_add.errors})


@api_view(["PUT"])
def update_student(request, id):
    current_data = Student.objects.get(id=id)
    new_data = request.data

    serialize_and_update = student_Serialize(current_data, data=new_data, partial=True)
    if serialize_and_update.is_valid():
        serialize_and_update.save()
        return Response({"message": "Student updated successfully!", "data":serialize_and_update.data})
    else:
        return Response({"message":"Error while updating!", "errors":serialize_and_update.errors})


@api_view(["DELETE"])
def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return Response({"message": "student deleted successfully!"})