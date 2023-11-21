from django.shortcuts import render , HttpResponse ,redirect
from datetime import datetime
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from math import ceil


def index(request):

    return render(request,"index.html")

def category(request):
    return render(request,"category.html")

def contactus(request):
    return render(request,"contactus.html")

def login(request):
    return render(request,"login.html")

def profile(request):
    return render(request,"profile.html")

def services(request):
    return render(request,"services.html")


def courses(request):
    return render(request,"courses.html")


