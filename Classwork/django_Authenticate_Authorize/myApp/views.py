from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginPage(request):
    if request.POST:
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        # print(user)
        if user is not None:
            login(request,user) # create the user session in browser.
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid Credentials!!"}) # if authentication fails then again render login page with error message.
        
    return render(request, "login.html")

def registerPage(request):
    if request.POST:
        data = request.POST
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        print(username, email, password)

        newUser = User(username=username, email=email)
        newUser.set_password(password) # stores a hashed password instead of full original password.
        newUser.save()
        return redirect("login") # redirect to login page once successfully registered.

    return render(request, "register.html") # render register page when visited the register url.


def homePage(request):
    return render(request, "home.html")

@login_required(login_url="login") # check if user is in session (logedin) only then it allows the access. if not loged then redirects to /login url
def dashboard(request):
    return render(request, "data.html")

def logoutLink(request):
    logout(request) # end the session in browser. 
    return render(request, "login.html")