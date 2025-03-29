from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib import messages

def home(request):
    return render(request,'impulsStranica/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('ImpulsStranica:home')
        else:
            messages.error(request, 'Neispravni podaci.')
    return render(request, 'login_register/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Korisničko ime već postoji.')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('ImpulsStranica:home')
    return render(request, 'login_register/register.html')