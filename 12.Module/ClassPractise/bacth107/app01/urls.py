from django.urls import path
from . import views

urlpatterns = [
    path('about-us',views.home, name='home'),
    path('',views.home, name='home'),

    path('contact01',views.contact, name='contact'),

    path('homepage',views.homepage, name='homepage'),
  
    
]