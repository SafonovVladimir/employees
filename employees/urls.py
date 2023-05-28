from django.urls import path

from employees.views import (
    index,
    user_login,
    user_logout,
    register,
    validate_username,
    check_username,
    EmployeeListView,
    EmployeeDetailView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
    employee_hierarchy,
    PositionListView,
    PositionDetailView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
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

    path("positions/", PositionListView.as_view(), name="positions-list"),
    path("positions/<int:pk>/", PositionDetailView.as_view(), name="positions-detail"),
    path("positions/create/", PositionCreateView.as_view(), name="positions-create"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="positions-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="positions-delete"),

    path("hierarchy/", employee_hierarchy, name="employees-hierarchy"),
]

app_name = "employees"
