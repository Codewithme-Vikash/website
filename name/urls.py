from unicodedata import name
from django.contrib import admin
from django.urls import path
from name import views

urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('servies',views.servies,name="servies"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    
]