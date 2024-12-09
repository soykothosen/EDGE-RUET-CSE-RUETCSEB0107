from django.urls import path
from . import views

urlpatterns = [
    path('about-us',views.home, name='home'),
    path('',views.home, name='home'),
  
    
]