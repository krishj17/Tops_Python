from django.shortcuts import render,redirect
from formApp.models import *

# Create your views here.
def index(request):
    return render(request, "index.html")


def register(request):
    data = request.POST
    id = data.get("id")
    name = data.get("userName")
    email = data.get("userEmail") 
    phone = data.get("userPhone")
    age = data.get("userAge")
    if id:  # if updating then post will send a valid id from the hidden input field.
        s = Student.objects.get(id=id)
        s.name = name
        s.email=email
        s.phone=phone
        s.age=age
        s.save()
        return render(request, "index.html", {"message":"Updated Successfully!!"})
    else:
        s = Student(name=name, email=email, phone=phone, age=age)
        s.save()
        return render(request, "index.html", {"message":"Registered Successfully!!"})
    

def display(request):
    data = Student.objects.all()
    return render(request, "display.html", {"data": data})


def deleteData(request):   
    id = request.GET["id"] # get id from route params.
    student = Student.objects.get(id=id)   # find the student data from id and delete.
    student.delete()
    return redirect("display")  # redirect to display route.


def updateData(request):  # populate old data to index register form.
    id = request.GET['id']
    student = Student.objects.get(id=id)
    return render(request, "index.html", {"sData": student})