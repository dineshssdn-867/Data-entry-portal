from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def main_view(request):
    return render(request, "login/login.html")


def login_vew(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('data_entry:main')
    else:
        return render(request, "login/login.html")


@login_required(login_url='index')
def logout_request(request):
    logout(request)
    return redirect("login:index")
