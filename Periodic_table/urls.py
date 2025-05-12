from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path('registration/',views.registration),
    path('menu/',views.menu),
    path('login/',views.login),
     path('menu/Location',views.Location),
    path('menu/diet/',views.diet),
    path('Location/',views.Location),
    path('registration/login/',views.login),
    path('registration/login/menu/',views.menu),
    path('login/menu/',views.menu),
    path('registration/login/menu/diet',views.diet),
    path('registration/login/menu/Location',views.Location),
    path('registration/home/',views.home),
    path('login/home/',views.home),
    path('Location/menu/',views.menu),
    path('login/menu/Location/',views.Location),
    path('diet/menu/',views.menu),
    path('registration/login/menu/diet/menu/',views.menu),
    path('login/menu/diet/menu/',views.menu),
    path('login/menu/diet/',views.diet),
    path('registration/login/menu/Location/menu/',views.menu),
    path('login/menu/Location/Menu/',views.menu),
    path('registration/login/home/',views.home),
    

]