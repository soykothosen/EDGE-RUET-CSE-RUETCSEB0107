from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse ("Hi")

def contact(request):
    return HttpResponse ("<h1>Contact Page </h1>")

def homepage(request):
    return render(request,'home.html')


