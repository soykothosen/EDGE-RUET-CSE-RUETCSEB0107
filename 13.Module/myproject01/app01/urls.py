from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'), 
    path('newpage',views.newpageh, name='newpageh'), 
    path('htmlpage',views.htmlpagesend, name='htmlpagesend'),
    path('page02',views.page02, name='page02'),  

   
    
]