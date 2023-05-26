from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from employees.forms import UserLoginForm, UserRegisterForm, EmployeeForm
from employees.models import Employee


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


class EmployeeListView(LoginRequiredMixin, generic.ListView):
    model = Employee
    paginate_by = 25

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(EmployeeListView, self).get_context_data(**kwargs)
    #
    #     model = self.request.GET.get("model", "")
    #
    #     context["search_form"] = CarModelSearchForm(initial={
    #         "model": model
    #     })
    #     return context
    #
    # def get_queryset(self):
    #     queryset = Car.objects.select_related("manufacturer")
    #     form = CarModelSearchForm(self.request.GET)
    #
    #     if form.is_valid():
    #         return queryset.filter(
    #             model__icontains=form.cleaned_data["model"]
    #         )


class EmployeeDetailView(LoginRequiredMixin, generic.DetailView):
    model = Employee


class EmployeeCreateView(LoginRequiredMixin, generic.CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("employees:employees-list")


class EmployeeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("employees:employees-list")


class EmployeeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Employee
    success_url = reverse_lazy("employees:employees-list")
