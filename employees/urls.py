from django.urls import path

from employees.views import (
    index,
    user_login,
    user_logout,
    register,
    validate_username,
    check_username
)

urlpatterns = [
    path("", index, name="index"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
    path("validate_username/", validate_username, name="validate_username"),
    path("check_username/", check_username, name="check_username"),
]

app_name = "employees"
