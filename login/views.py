from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def main_view(request):
    return render(request, "login/login.html")


def login_vew(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return redirect('data_entry:main')
    else:
        return render(request, "login/login.html")


@login_required(login_url='login:index')
def logout_request(request):
    logout(request)
    return redirect("login:index")
