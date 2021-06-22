from django.contrib import admin
from django.urls import path, include
from App import views

app_name='App'
urlpatterns = [
    path('home/', views.index, name='index'),
    path('login/', views.Log_in, name='Log_in'),
    path('logout/', views.user_logout, name='user_logout'),


]
