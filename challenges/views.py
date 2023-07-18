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
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


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

def getServices(request):
    services = Service.objects.all()
    return render(request, "services.html", {'services': services})

def submitAppointment(request):
   # services = Service.objects.values_list('name', flat=True) #flat=true returns a list instead of a turple
    services= Service.objects.all()
    if request.method == 'POST':
        names = request.POST['names']
        email = request.POST['email']
        hairstyle = request.POST['hairstyle']
        date_selected = request.POST['date']
        message = request.POST['message']

        if not names or not email or not hairstyle or not date_selected or not message:
            messages.error(request, "Please fill in all the fields")
        else:
            try:
                validate_email(email)
            except ValidationError:
                messages.error(request, "Please enter a valid email address")
            else:
                try:
                    service = services.get(name=hairstyle)
                except Service.DoesNotExist:
                    messages.error(request, "Invalid hairstyle selected.")
                else:
                    try:
                        customer = Customer.objects.get(email=email)
                    except Customer.DoesNotExist:
                        customer = Customer(first_name=names, email=email)
                        customer.save()
                    appointment = Appointment(service=service, customer=customer, scheduled_date = date_selected)
                    appointment.save()
                    messages.success(request, "Appointment created successfully!")
                    return redirect('contact')
        
    return redirect('contact')

def getOptions(request):
    services = Service.objects.all()
    return render(request, 'contact.html', {'services': services})