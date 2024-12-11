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



