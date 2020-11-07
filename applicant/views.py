from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Applicant_details, Feedback

import joblib
import pandas as pd
#reloadModel = joblib.load('')


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
    return render(request, 'feedback.html')


def suggestcourse(request):
    print (request)
    if request.method == 'POST':
        temp={}
        temp['empid']=request.POST.get('one')
        temp['commskill']=request.POST.get('two')
        temp['ethics']=request.POST.get('three')
        temp['knowledge']=request.POST.get('four')
        temp['listen']=request.POST.get('five')
        temp['job']=request.POST.get('six')
        temp['overall']=request.POST.get('seven')


    testData=pd.DataFrame(['x':temp]).transpose()
    scoreval = reloadModel.predict(testData)[0]
    context={'scoreval':scoreval}
    return render(request,'feedback.html')