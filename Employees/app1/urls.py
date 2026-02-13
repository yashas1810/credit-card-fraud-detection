from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("task/",views.task)
    path("ShowEmployee/",views.Show_employee)
]
