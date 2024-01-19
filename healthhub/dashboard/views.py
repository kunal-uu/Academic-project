from django.shortcuts import render, HttpResponse,redirect
from dashboard.models import *
# Create your views here.
def profile(request):
    return render(request,'profile.html')


def info(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        weight=request.POST['weight']
        height=request.POST['height']
        age=request.POST['age']
        goal=request.POST['goal']
        time=request.POST['time']
        #uservalid=True
        new=details(st_fullname=fullname,st_weight=weight,st_height=height,st_age=age,st_goal=goal,st_time=time).save()
        my_model= details.objects.all()
        return render(request,'profile.html')
    return render(request,'info.html')