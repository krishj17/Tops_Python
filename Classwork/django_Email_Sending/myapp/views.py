from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, "index.html")

def submit(request):
    email = request.GET["email"]
    send_mail("Testing Subject", "Sign Up successfull", settings.EMAIL_HOST_USER, [email])
    return render(request, "index.html")