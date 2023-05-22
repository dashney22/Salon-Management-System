from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') #If data supplied is in the correct format, then we send you to login page
        else:
            messages.error(request, "Invalid User Registration data")
            return redirect('register')
    else:
        form = UserCreationForm()  # Give the user an empty form since they did not post anything
        return render(request,"accounts/register.html",{'form':form})