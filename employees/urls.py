from django.urls import path

from employees.views import (
    index,
    user_login,
    user_logout,
    register,
    validate_username,
    check_username, EmployeeListView, EmployeeDetailView, EmployeeCreateView,
    EmployeeUpdateView, EmployeeDeleteView
)

urlpatterns = [
    path("", index, name="index"),

    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", register, name="register"),
    path("validate_username/", validate_username, name="validate_username"),
    path("check_username/", check_username, name="check_username"),

    path("employees/", EmployeeListView.as_view(), name="employees-list"),
    path("employees/<int:pk>/", EmployeeDetailView.as_view(), name="employee-detail"),
    path("employees/create/", EmployeeCreateView.as_view(), name="employee-create"),
    path("employees/<int:pk>/update/", EmployeeUpdateView.as_view(), name="employee-update"),
    path("employees/<int:pk>/delete/", EmployeeDeleteView.as_view(), name="employee-delete"),
]

app_name = "employees"
