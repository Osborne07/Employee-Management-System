from django.shortcuts import render, HttpResponse
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Emp.objects.all()
    context={
        'emps': emps
    }
    print(context)
    return render(request,'view_all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        role = int(request.POST['role'])
        dept = int(request.POST['dept'])

        new_emp = Emp(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,role_id=role,dept_id=dept, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("Employee added successfully")
    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("An exception Occured")

def remove_emp(request):
    return render(request,'remove_emp.html')

def filter_emp(request):
    return render(request,'filter_emp.html')