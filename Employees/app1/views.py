from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("hello")
def task(request):
    return render(request,'Home.html')
def Show_employee(request):
    Emp=Employees.objects.all()
    return render(request,'show.html',{'Employee':Emp})
