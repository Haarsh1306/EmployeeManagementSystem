from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addEmp", views.addEmp, name="addEmp"),
    path("viewEmp", views.viewEmp, name="viewEmp"),
    path("remEmp", views.remEmp, name="remEmp"),
    path("remEmp/<int:empId>", views.remEmp, name="remEmp"),
    path("filterEmp", views.filterEmp, name="filterEmp"),
]
