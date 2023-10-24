from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . forms import UserRegisterForm
from django.contrib.auth.models import User

def user(request):
    cureent_user = request.user, 
    all_users = User.objects.all()
    return render(request, 'user.html', {'user' : cureent_user, 'all_users' : all_users})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirmpassword = form.cleaned_data['confirmpassword']
            
            if password == confirmpassword:
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, 'Register Berhasil')
            else:
                messages.error(request, 'Password dan konfirmasi passwword tidak sesuai')
                return render(request, 'register.html', {'form' : form})
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form' : form})        

def delete(request):
    user = get_object_or_404(User, id=id)
    user.delete()
    return render('user')

