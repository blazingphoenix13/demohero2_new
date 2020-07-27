from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    return render(request,'emp/home.html')

def dashboard(request):
    emp = EmpModel.objects.all()
    context = {'empdata':emp}
    return render(request,'emp/dashboard.html',context)