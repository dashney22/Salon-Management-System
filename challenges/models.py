from django.db import models
from django.utils import timezone

#This one was meant for testing purposes
class Book(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    description = models.TextField(max_length=255, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=3)
    publishedDate = models.DateField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(blank=True, upload_to='covers/')

    def __str__(self):       # This code helps modify the look o
        return self.name

# CUSTOMER Table...
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    # Add more fields as per your requirements
    def __str__(self):
        return self.first_name

# STAFF MEMBERS
class StaffMember(models.Model):
    POSITION_CHOICES = [
        ('cleaner', 'Custodian'),
        ('junior_beauty_technician', 'Junior Beauty Technician'),
        ('braiding_specialist', 'Braiding Specialist'),
         ('senior_hair_stylist', 'Senior Hair Stylist'),
        ('manager', 'Manager'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    staff_image = models.ImageField(upload_to='staff/images', blank=True)
    phone_number = models.CharField(max_length=20)
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    date_of_birth = models.DateField()
    # Add more fields as per your requirements

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Services offered by the salon
class Service(models.Model):
    STYLE_CHOICES = [
        ('bantu_knots', 'Bantu Knots'),
        ('box_braids', 'Box Braids'),
        ('feed_in_braids', 'Feed-in Braids'),
        ('tribal_braids', 'Tribal Braids'),
        ('passion_twists', 'Passion Twists'),
    ]
    name = models.CharField(max_length=100, choices=STYLE_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in minutes")
    image = models.ImageField(upload_to="img", default="img/chuenza.PNG")

    def __str__(self):
        return self.name
    
#Bookings Table
class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(default=timezone.now)
    scheduled_date = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.customer.first_name} - {self.service.name}"
