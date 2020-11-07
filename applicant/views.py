from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Applicant_details, Feedback


def applicant_login(request):
    if request.method == 'POST':
        appno = request.POST.get('application_no')
        phno = request.POST.get('phone_no')
       
        print(appno)
        print(phno)

    
        if Applicant_details.objects.filter(application_no=appno, phone_no=phno):
            return redirect('applicant_home')
        
        else:
            messages.info(request, 'Invalid Credentials')



    return render(request, 'applicant_login.html')



def applicant_home(request):
    return render(request, 'applicant_home.html')



def applicant_logout(request):
    return render(request, 'logout.html')


def feedback(request):
    context = {'a':'HelloWorld'}
    return render(request, 'feedback.html',context)


def suggestcourse(request):
    return None