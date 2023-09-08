from django.urls import path 
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('profile/', views.profile, name='profile'),
    path('logoutUser/', views.logoutuser, name='logoutUser'),
]