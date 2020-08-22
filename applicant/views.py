from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Applicant_details, Feedback


def applicant_login(request):
    if request.method == 'POST':
        appno = request.POST.get('application_no')
        phno = request.POST.get('phone_no')
        print('h111')
        print(appno)
        print(phno)

    
        if Applicant_details.objects.filter(application_no=appno, phone_no=phno):
            print('HI')
        
            return redirect('applicant_home')
        
        else:
            messages.info(request, 'Invalid Credentials')
            print('HI3')


    else:
        print('HI4')

    return render(request, 'content/applicant_login.html')



def applicant_home(request):
    return render(request, 'content/applicant_home.html')


def applicant_feedback(request):
    if request.method == 'POST':

        one= request.POST.get('one')
        two= request.POST.get('two')
        three= request.POST.get('three')
        four= request.POST.get('four')
        five= request.POST.get('five')
        six= request.POST.get('six')


        fb_values = Feedback.objects.create(one=one,two=two,three=three,four=four,five=five,six=six)
        fb_values.save()
        return render(request, 'content/feedback.html')
    else:
        return render (request, 'content/feedback.html')


def applicant_logout(request):
    return render(request, 'content/logout.html')