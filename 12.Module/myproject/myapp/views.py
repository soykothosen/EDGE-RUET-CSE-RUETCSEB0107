from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Hello World")

def home(request):
    return HttpResponse("<h1>Hello World</h1>")

def home(request):
    return render(request,'home.html',{'name': 'Test Name'})

def newpage(request):
    return render(request,'index.html',{'name': 'Test Name'})

def add(request):
    #var1 = int(request.GET['num1'])
    #var2 = int(request.GET['num2'])

    var1 = int(request.POST['num1'])
    var2 = int(request.POST['num2'])
    
    sum = var1 + var2

    return render(request,'result.html', {'result':sum})
