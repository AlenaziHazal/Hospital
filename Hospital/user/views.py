from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def login_view(request:HttpRequest):
    massage = ''
    if request.method == 'POST':
        try:
            user = authenticate(request, username=request.POST['username'],password=request.POST['password'])

            if user:
                login(request,user)
                return redirect('home:home_view')
            
        except Exception as e:
            massage = f'this error by {e}'
            return massage

    return render(request,'user/login.html',{'massage':massage})


def signup_view(request:HttpRequest):
    massage = ''
    
    return render(request,'user/signup.html',{'massage':massage})