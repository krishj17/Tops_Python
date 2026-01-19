from django.shortcuts import render
from studentApp.models import *
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, "index.html")


def addstudent(request):
    sname = request.POST['sname']
    sage = request.POST['sage']
    sphone = request.POST['sphone']
    print(sname, sage, sphone)
    sobj = Student(
        sName=sname,
        sAge=sage,
        sPhone=sphone
    )
    sobj.save()
    return JsonResponse({"message":"Student Saved Successfully!"})


def getstudent(request):
    studentData = Student.objects.all()
    # print(list(studentData.values()))
    return JsonResponse({"studentData": list(studentData.values())})


def deletestudent(request):
    studentId = request.GET['studentId']
    sobj = Student.objects.get(id=studentId)
    sobj.delete()
    return JsonResponse({"message": "Student Deleted Successfully!"})

def loadStudent(request):
    studentId = request.GET['studentId']
    sobj = Student.objects.get(id=studentId)
    print("----------------",list(sobj))
    return JsonResponse({"studentData":sobj})


