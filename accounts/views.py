from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse, reverse_lazy

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
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, "login.html", {}) # USer just went to the page!!!!

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('home'))