from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Applicant_details, Feedback

import pandas as pd


def applicant_login(request):
    if request.method == 'POST':
        appno = request.POST.get('application_no')
        phno = request.POST.get('phone_no')
       
        print(appno)
        print(phno)

    
        if Applicant_details.objects.filter(application_no=appno, phone_no=phno):
            return render(request, 'applicant_home.html')
        
        else:
            messages.info(request, 'Invalid Credentials')



    return render(request, 'applicant_login.html')



def applicant_home(request):
    return render(request, 'applicant_home.html')



def applicant_logout(request):
    return render(request, 'logout.html')


def feedback(request):
    if request.method == 'POST':

        one= request.POST.get('one')
        two= request.POST.get('two')
        three= request.POST.get('three')
        four= request.POST.get('four')
        five= request.POST.get('five')
        six= request.POST.get('six')


        fb_values = Feedback.objects.create(one=one,two=two,three=three,four=four,five=five,six=six)
        fb_values.save()
        return render(request, 'feedback.html')
    else:
        return render (request, 'feedback.html')
