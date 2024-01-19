from django.shortcuts import render, HttpResponse,redirect
from authenticate.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def login(request):
    if request.method=='POST':
        user=request.POST['username']
        passw=request.POST['password']
        user=authenticate(request,user_username=user,user_password=passw)
        if user is not None:
            # login(request,user)
            # messages.success(request,"Successfully Login")
            return render('C:/Users/gaurav kumar/Desktop/Major Project/healthhub/dashboard/templates/info.html')
        else:
            messages.error(request,'Username or Password is Incorrect!')
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        
        if password!=confirmpassword:
            messages.error("Your password and confirm password are not matched!")
        else:
            my_user=User(user_username=username,user_email=email,user_password=password,user_confirmpassword=confirmpassword).save()  
            my_user= User.objects.all()
            messages.success(request,'Your Account Successfully Created!')
            #print(username,email,password,confirmpassword,)
            return redirect('loginpage')
    return render(request,'register.html')



    

def contact(request):
    return render(request,'contact.html')


   

