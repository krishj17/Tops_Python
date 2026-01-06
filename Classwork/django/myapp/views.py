from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")  # renders index.html file from templates folder, which is already set in settings.

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def help(request):
    return render(request, "help.html")
