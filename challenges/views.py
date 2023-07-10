from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from .models import *
from rest_framework import viewsets, status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import updateAppointment
from django.contrib import messages
from django.urls import reverse


@login_required
def HomePage(request):
    return render(request,'index.html')

@login_required
def about_us(request):
    return render(request, 'about.html')

@login_required
def update_appoitnment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id) #First get the appointment

    if request.method == 'POST':
        form = updateAppointment(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments')
        else:
            messages.error(request, 'Enter correct Details')
            return redirect(reverse('update_appointment'))
        
    else:
        form = updateAppointment(instance=appointment)

    return render(request, 'update_appointment.html',{'form':form})

@login_required
def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})

