from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def home_view(request:HttpRequest):
    
    hospital = User.objects.filter(groups__name ='hospital')

    return render(request,'home/home.html',{'hospital':hospital})