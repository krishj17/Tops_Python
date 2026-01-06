from django.urls import path
from myApp.views import *

urlpatterns = [
    path('', homePage, name="home"),
    path('login', loginPage, name="login"),
    path('register', registerPage, name="register"),
    path('dashboard', dashboard, name="dashboard"),
    path('logout', logoutLink, name="logout")
]
