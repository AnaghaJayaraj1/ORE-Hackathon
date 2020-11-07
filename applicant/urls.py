from django.urls import path
from . import views
from django.conf.urls import url
from applicant import views

app_name = 'applicant'

urlpatterns = [
    path('applicant_login/', views.applicant_login, name='applicant_login'),
    path('applicant_home/', views.applicant_home, name='applicant_home'),
    path('logout/', views.applicant_logout, name='applicant_logout'),
    path('feedback/', views.feedback, name='feedback.html'),
]
