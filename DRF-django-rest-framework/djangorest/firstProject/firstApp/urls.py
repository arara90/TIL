from django.contrib import admin
from django.urls import path
from firstApp import views

urlpatterns = [
    path('emps/', views.employeeView)
]
