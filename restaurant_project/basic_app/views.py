from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from basic_app.models import UserRegistration

# Create your views here. 

def index(request):
    return render(request,"Foodie/index.html")

def signUp(request):
    if request.method == 'POST':
        username=request.POST.get('user_email')
        password=request.POST.get('user_password')
        try:
            user = User.objects.get(username=username)
            print(user)
            user = authenticate(request,username=username,password=password)
            auth.login(request, user)
            if user.is_authenticated:
                print("Logged In")
                user_logged = request.user
                user_profile = UserRegistration.objects.get(user=user_logged)
                print(" ASDJKSAjdkl ",user_profile)
                return render(request,'Foodie/emp_profile.html',context={'user':user_logged,'user_profile':user_profile})

        except:
            print("User not exist")
            try:
                user = User.objects.get(username=username)
                print(user)
                if user.is_active == False:
                    errormsg = 'Email or Password Incorrect'
            except:        
                errormsg = 'User Does Not Exists'
            
                return render(request, 'Foodie/index.html', { 'errormsg':errormsg})
              
    return render(request, 'Foodie/index.html')        

def logout_user(request):
    auth.logout(request)
    print("LogOut")
    return redirect(index)


def profile_page(request):
    user = request.user
    user_profile = UserRegistration.objects.filter(curr_user=user)
    print(" ASDJKSAjdkl ",user_profile)
    return render(request,'Foodie/emp_profile.html',context={'user':user,'user_profile':user_profile})


def training(request):
    return render(request,'Foodie/Courses.html')


def reports(request):    
    return render(request,'Foodie/reports.html')


def rewards(request):
    return render(request,'Foodie/reward.html')