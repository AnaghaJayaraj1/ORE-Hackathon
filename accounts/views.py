from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate

from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect


#@cache_page(60 * 15)
@csrf_protect
def login(request):
    
    if request.method == 'POST':
        
        username= request.POST['email']
        password = request.POST['password']
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
           
            return redirect("dashboard")
        else:
            
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def dashboard(request):
    return render (request, 'team_dashboard.html')


def dashboard_enterapplication(request):
    return render (request, 'enterapplication.html')



def profile(request):
    return render(request, 'profile.html')