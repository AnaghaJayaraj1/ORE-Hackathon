from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from application.models import Application
import fingerprint


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('emailid')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('helo')
    fprint = fingerprint.Fingerprint(
        kgram_len=4, window_len=5, base=10, modulo=1000)
    print(fprint)

    return render(request, 'content/login.html')


@login_required(login_url='/login/')
def dashboard(request):
    count = Application.objects.values('empid').distinct().count()
    c1 = Application.objects.values('empid').count()
    c2 = Application.objects.filter(action='A').count()
    c3 = Application.objects.filter(action='V').count()

    k = Application.objects.values()
    dashboard1 = {}
    dashboard2 = {}
    dashboard3 = {}
    for i in range(count):
        dashboard1[i] = {
            'Name': k[i].get('name'),
            'PN': Application.objects.filter(empid=k[i].get('empid')).count(),
        }
    for i in range(count):
        if k[i].get('action') == 'A':
            dashboard2[i] = {
                'Name': k[i].get('name'),
                'PN': Application.objects.filter(empid=k[i].get('empid'), action='A').count(),
            }
    for i in range(count):
        if k[i].get('action') == 'V':
            dashboard3[i] = {
                'Name': k[i].get('name'),
                'PN': Application.objects.filter(empid=k[i].get('empid'), action='V').count(),
            }

    context = {
        'D1': dashboard1,
        'C1': c1,
        'C2': c2,
        'D2': dashboard2,
        'C3': c3,
        'D3': dashboard3,
        'P': 0
    }

    return render(request, 'content/dashboard.html', context)
