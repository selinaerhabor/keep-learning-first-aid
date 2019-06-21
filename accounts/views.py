from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserAccountForm, UserRegistrationForm

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
    if request.method == "POST":
        account_form = UserAccountForm(request.POST)
        if account_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
            else:
                account_form.add_error(None, "Your username or password is incorrect")
    else:
        account_form = UserAccountForm()
    return render(request, 'login.html', {"account_form": account_form})

#For Register Tab
def registration(request):
    registration_form = UserRegistrationForm()
    return render(request, 'registration.html',
    {"registration_form": registration_form})
    
#For Profile
def user_profile(request):
    user_profile = AccountProfile()
    return render(request, 'profile.html',
    {"account_profile": account_profile})
    