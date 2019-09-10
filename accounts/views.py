from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserAccountForm, UserRegistrationForm
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

    
#For Log out Tab
def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return render(request, 'index.html')
    
#For Log in Tab
def login(request):
    if request.method == "POST":
        account_form = UserAccountForm(request.POST)
        if account_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return render(request, 'index.html')
            else:
                account_form.add_error(None, "Your username or password is incorrect")
    else:
        account_form = UserAccountForm()
    return render(request, 'login.html', {"account_form": account_form})

#For Register Tab
def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
                                    
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, 
                "System could not register your account at this time. Please try again later.")
                
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html',
        {"registration_form": registration_form})
    
#For User Profile
def profile(request):
    return render(request, 'profile.html')
    
#For Register Tab
def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
                                    
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
            else:
                messages.error(request, 
                "System could not register your account at this time. Please try again later.")
                
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html',
        {"registration_form": registration_form})
    