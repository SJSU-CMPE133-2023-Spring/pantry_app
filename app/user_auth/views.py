from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm


def login_view(request):
    if request.method == 'POST':
        print("got this far")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/pantry/')
        else:
            err_m = "Failed to login. Invalid Credentials"
    
    form = AuthenticationForm()
    return render(request, 'user_auth/login.html', {'form': form, 'err_m': err_m})



def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/pantry/')
    else:
        form = RegistrationForm()
        return render(request, 'user_auth/register.html', {'form': form})