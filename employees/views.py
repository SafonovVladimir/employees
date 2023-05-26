from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect

from employees.forms import UserLoginForm, UserRegisterForm


def index(request):
    """View function for the home page of the site."""
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_visits": num_visits + 1,
    }

    return render(request, "employees/index.html", context=context)


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("employees:index")
    else:
        form = UserLoginForm()
    return render(request, "employees/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("employees:login")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        context = {
            "form": form,
        }
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("employees:index")
        else:
            messages.error(request, "Error")
    else:
        form = UserRegisterForm()
        context = {
            "form": form,
        }
    return render(request, "employees/register.html", context=context)


def validate_username(request):
    """Check available name"""
    username = request.GET.get("username", None)
    response = {
        "is_taken": User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)


def check_username(request):
    """Check name"""
    username = request.GET.get("username", None)
    response = {
        "is_taken": User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(response)
