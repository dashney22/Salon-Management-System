from django.urls import path, include
from .views import *
from rest_framework import routers

urlpatterns = [
     path('books/', firstFunction, name="home"),
     path('about/', about_us, name='about'),
     path('appointments/', appointments, name='appointments'),
]