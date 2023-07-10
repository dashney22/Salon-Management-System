from .models import Appointment, Service
from django import forms

class updateAppointment(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service','customer','scheduled_date']