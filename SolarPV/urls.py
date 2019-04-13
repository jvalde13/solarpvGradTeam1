		#from django.contrib import admin
from django.urls import path

#from hello.views import greeting
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('default/', views.default, name='home'),
    path('home/', views.home , name='home'),
    path('login/', views.login, name='login'),
    path('JoinUS/', views.JoinUS, name='JoinUS'),
    path('email/', views.email , name='email'),    
]
 