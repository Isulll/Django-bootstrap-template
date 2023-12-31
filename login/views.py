from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from . forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Login Berhasil')
                return redirect('dashboard')
            else:
                messages.error(request, 'Username atau password yang dimasukkan salah')
    else:
        form = UserLoginForm()
        
    return render(request, 'login.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('login')