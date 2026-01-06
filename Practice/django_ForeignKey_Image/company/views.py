from django.shortcuts import render, redirect
from company.models import *
# Create your views here.
def index(request):
    departData = Department.objects.all()
    return render(request, 'index.html', {'allDepartData': departData})

def display(request):
    departData = Department.objects.all()
    empData = Employee.objects.all()
    return render(request, 'display.html', {'departData':departData, 'empData':empData})

# Department Related Views

def addDepart(request):
    data = request.POST
    DepartId = data.get('Did')
    departName = data.get('Dname')
    if DepartId:
        dobj = Department.objects.get(id=DepartId)
        dobj.departName=departName
        dobj.save()
        return render(request, 'index.html', {'message': 'Department Updated!!'})
    else:
        dobj = Department(departName=departName)
        dobj.save()
        return render(request, 'index.html', {'message': 'Department Added!!'})

def updateDepart(request):
    DepartId = request.GET['id']
    DepartData = Department.objects.get(id=DepartId)
    return render(request, 'index.html', {'DepartData': DepartData})

def removeDepart(request):
    DepartId =request.GET['id']
    DepartData = Department.objects.get(id=DepartId)
    DepartData.delete()
    return redirect('display')


# Employee Related Views

def addEmp(request):
    data = request.POST
    empId = data.get('Eid')
    empName = data.get('Ename')
    empAge = data.get('Eage')
    empSalary = data.get('Esalary')
    empimage = request.FILES.get('Eimage')
    empDepart = data.get('Edepart')
    empDepartInstance = Department.objects.get(id=empDepart) # we need the instance to add foreign key.

    if empId:
        empData = Employee.objects.get(id=empId)
        empData.empName = empName
        empData.empAge = empAge
        empData.empSalary = empSalary
        empData.empDepart = empDepartInstance
        if empimage:
            empData.empImage.delete(save=False) # delete from the media/images and database.
            empData.empImage=empimage  # set the new image.
            
        empData.save()
        return render(request, 'index.html', {'message': 'Employee Updated!!'})
    else:
        empData = Employee(empName=empName, empImage=empimage, empDepart=empDepartInstance, empAge=empAge, empSalary=empSalary)
        empData.save()
        return render(request, 'index.html', {'message': 'Employee Data Added!!'})


def updateEmp(request):
    empId = request.GET['id']
    empData = Employee.objects.get(id=empId)
    allDepartData = Department.objects.all()
    return render(request, 'index.html', {'empData': empData, 'allDepartData': allDepartData})


def deleteEmp(request):
    empId = request.GET['id']
    eobj = Employee.objects.get(id=empId)
    eobj.delete()
    return redirect('display')