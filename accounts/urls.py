from django.urls import path
from . import views


urlpatterns=[
    path('login/', views.login, name = 'login'),
    path('dashboard/profile/', views.profile, name = 'profile'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('dashboard/EnterApplication', views.dashboard_enterapplication, name = 'dashboard_enterapplication'),
    
] 