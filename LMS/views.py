from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def login_(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST.get('pass')
        student = authenticate(username=u, password=p)
        if student is not None:
            login(request, student)
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'username or password does not match')
            return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'index.html')
