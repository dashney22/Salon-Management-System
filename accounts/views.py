from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
#Get your about us page



def login_view(request):
    if request.method== "POST":  #if user filled out the form do the following
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Enter correct username or password')
            return redirect(reverse('login'))
    else:
        return render(request, "accounts/login.html", {}) # User just went to the page!!!!

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('home'))

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm = request.POST['confirm_password']

        #Check if the passwords match
        if password==confirm:
            #check is user exists in the database:
            if User.objects.filter(username=username).exists():
                messages.error(request, "User Already Exists")
            else:
                #create user and redirect to login
                User.objects.create_user(username=username, password=password)
                messages.success(request, "User Created Successfully")
                return redirect('login')
       
    return render(request,"accounts/register.html")