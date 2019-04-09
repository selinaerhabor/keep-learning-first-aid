from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

# Create your views here.

#Home Page
def index(request):
    return render(request, 'index.html')
    
#For Log out Tab
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
    
#For Log in Tab
def login(request):
    return render(request,'login.html')