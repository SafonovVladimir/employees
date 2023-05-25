from django.urls import path

from employees.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "employees"
