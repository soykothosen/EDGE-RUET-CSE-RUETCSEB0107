from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse ("Hi")

def newpageh(request):
    return HttpResponse ("<h1> Hi </h1>")

# def htmlpagesend(request):
#     return render(request,'home.html')

def htmlpagesend(request):
    return render(request,'home.html',{'name1': 'Test Name', 'name2': "Soykot"})

def page02(request):
    return render(request,'page02.html')

def add(request):

    # number1 = int(request.GET['num1'])
    # number2 = int(request.GET['num2'])

    number1 = int(request.POST['num1'])
    number2 = int(request.POST['num2'])

    sum = number1 + number2 


    return render(request,'result.html', {'result': sum})



