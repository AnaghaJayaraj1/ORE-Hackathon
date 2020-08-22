from django.urls import path
from . import views


urlpatterns = [
    path('applicant_login/', views.applicant_login, name='applicant_login'),
    path('applicant_home/', views.applicant_home, name='applicant_home'),
    path('applicant_feedback/', views.applicant_feedback, name='applicant_feedback'),
    path('logout/', views.applicant_logout, name='applicant_logout'),


]
