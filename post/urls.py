from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('add/', views.add_post, name='add_post'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_logout/', views.user_logout, name='logout'),
]