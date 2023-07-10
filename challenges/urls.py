from django.urls import path, include
from .views import *
from rest_framework import routers

urlpatterns = [
     path('home/', HomePage, name="home"),
     path('about/', about_us, name='about'),
     path('appointments/', appointments, name='appointments'),
     path('services/',getServices, name='services'),
     path('appointment/<int:appointment_id>/update', update_appoitnment, name='update_appointment'),
]