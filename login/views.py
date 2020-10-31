from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import loginform



def main_view(request):
    return render(request, "login/login.html")

def login_vew(request):
    form = loginform(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('main')
    else:
        context = {
            'form': form
        }
        messages.MessageFailure("No ")
        return render(request, 'login/login.html', context)


@user_passes_test(lambda u: u.is_superuser)
def register_view(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = form.save()
        login(request, user)
        return redirect("index")

    else:
        form = UserCreationForm()

    return render(request, 'login/register.html', {'form': form})


@login_required(login_url='index')
def logout_request(request):
    logout(request)
    return redirect("index")





