from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import *
from .form import StudentUserForm

def home(request):
    return render(request, "managementsystem/index.html")

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out Successfully")
    return redirect("/")

def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request, username=name, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in Successfully")
            return redirect("/")
        else:
            messages.error(request, "Invalid User Name or Password")
            return redirect("/login")
    return render(request, "managementsystem/login.html")

def register(request):
    form = StudentUserForm()

    if request.method == 'POST':
        form = StudentUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Success. You can Login Now...!")
            return redirect('/login')

    return render(request, 'managementsystem/register.html', {'form': form})
