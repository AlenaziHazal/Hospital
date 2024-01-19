from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User,Group
from django.contrib.auth import login, logout, authenticate
from .models import StudentProfile
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
    if request.method == 'POST':
        try:

            new_user = User.objects.create_user(username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            new_user.save()
            user_field = request.POST['selected_option']

            if user_field == 'student':
                if not new_user.groups.filter(name='student').exists():
                    group = Group.objects.get(name="student")
                    new_user.groups.add(group)

            elif user_field == 'hospital':
                if not new_user.groups.filter(name='hospital').exists():
                    group = Group.objects.get(name="hospital")
                    new_user.groups.add(group)
            
            new_user = authenticate(request, username=request.POST['username'],password=request.POST['password'])

            if new_user:
                login(request,new_user)
            
            if user_field == 'student':

                return redirect('user:profile_view',user_id=request.user.id)
            else:
                return redirect('home:home_view')
        
        except Exception as e:
            massage = f'this is th eroor'
            return massage
    
    return render(request,'user/signup.html',{'massage':massage})

def view_all_hospitals(request:HttpRequest):

    hospital = User.objects.filter(groups__name ='hospital')

    return redirect('home:home_view')

def logout_view(request:HttpRequest):

    if request.user.is_authenticated:

        logout(request)

        return redirect('user:login_view')
    
def profile_view(request:HttpRequest,user_id):
        
    msg = None
    user = User.objects.get(id=user_id)
    
    student = User.objects.filter(groups__name ='student')       

    if request.user in student:
        try:
            profile = request.user.StudentProfile
        except Exception:
            msg = 'Please update your profile'


    return render(request,'user/profile.html',{'user':user,'student':student,'massage':msg})


def update_profile_view(request:HttpRequest,user_id):

    user = User.objects.get(id=request.user.id)
    years = StudentProfile(user=user)
    if request.user.is_authenticated:
            if request.method == 'POST':

                user.first_name = request.POST['first_name']
                user.last_name =  request.POST['last_name']
                user.email = request.POST['email']

                user.save()

                try:
                    manager_profile=user.StudentProfile

                except Exception as e:
                        
                    manager_profile = StudentProfile(user=user)

                manager_profile.phone_number = request.POST['phone_number']
                manager_profile.major = request.POST['major']
                manager_profile.university_name = request.POST['university_name']
                manager_profile.x_link = request.POST['x_link']
                manager_profile.year_of_study = request.POST['year_of_study']
                manager_profile.cv = request.FILES['cv']
                manager_profile.linkedIn = request.POST['linkedIn']
                manager_profile.trascript = request.FILES['trascript']
                manager_profile.medical_health = request.FILES['medical_health']
                manager_profile.bio = request.POST['bio']                         
                                                            
                if 'manager_avatar' in request.FILES:

                        manager_profile.manager_avatar = request.FILES['manager_avatar']

                manager_profile.save()

                return redirect('user:profile_view',request.user.id)
    
    context = {
        'user':user,
        'years_of_studies':years.years_of_studies
    }                        
    return render(request,'user/update_profile.html',context)

def investors_view(request:HttpRequest):

    investors = User.objects.filter(groups__name ='hospital')

    return render(request,'user/investors.html',{'investors':investors})