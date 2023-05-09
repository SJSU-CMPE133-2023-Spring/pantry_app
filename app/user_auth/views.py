from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
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
        return redirect(request, 'pantry/construction.html', {})
    else:
        form = AuthenticationForm()
    return render(request, 'user_auth/login.html', {'form': form})


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