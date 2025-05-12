from django.urls import path
from django.shortcuts import render
from django.contrib import admin
def registration(request):
    return render(request ,'Registration.html')
def login(request):
    return render(request ,'login.html')
def home(request):
    return render(request ,'home.html')
def periodic_table(request):
    return render(request ,'periodic_table.html')
def Location(request):
    return render(request ,'Location.html')
def menu(request):
    return render(request ,'menu.html')
def diet(request):
    return render(request ,'diet.html')

