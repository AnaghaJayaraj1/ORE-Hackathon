from django.urls import path
from . import views


urlpatterns=[
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('dashboard/profile/', views.profile, name = 'profile'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    
] 