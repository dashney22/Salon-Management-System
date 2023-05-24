from django.contrib import admin
from .models import *

# Register your models here.
# Import model name (.[model_name] if they from the same folder!) admin.site.Register

admin.site.register(Book)

# Admin customisation

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration')
    list_filter = ('duration',)
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

@admin.register(StaffMember)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name','position')

@admin.register(Appointment)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('service','customer')

