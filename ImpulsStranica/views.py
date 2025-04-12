from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User,Work
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
from django.http import FileResponse


def home(request):
    return render(request,'impulsStranica/index.html')

def radovi(request):
    return render(request, 'impulsStranica/radovi.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('ImpulsStranica:ulogiran')
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

@login_required
def ulogiran_view(request):
    return render(request, 'korisnik_stranice/ulogiran.html')

@login_required
def upload_work(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')

        if title and file:
            work = Work.objects.create(
                user=request.user,
                title=title,
                file=file
            )
            return redirect('ImpulsStranica:ulogiran') 

    return render(request, 'ImpulsStranica:ulogiran')

@login_required
def ulogiran_view(request):
    user_works = Work.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'korisnik_stranice/ulogiran.html', {'user_works': user_works})

def Impuls_overview(request):
    return render(request, 'impulsStranica/upute.html')

def download_Impuls(request):
    file_path = os.path.join(
        settings.BASE_DIR, 'ImpulsStranica', 'static', 'pdfs', 'APA standardi prilikom pisanja rada_24_25.pdf'
    )
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='APA_standardi.pdf')