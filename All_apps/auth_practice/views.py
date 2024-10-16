from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/auth_practice/login/')
def home(request):
    return render(request, 'home.html')

def signup(request):
    if(request.method == 'POST'):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.error(request, 'alredy exist')
            # return redirect('/auth_practice/login/')
        else:
            user = User.objects.create(
                email = email,
                username = username
            )
            user.set_password(password)
            user.save()
            messages.success(request, 'user created !')

            return redirect('/auth_practice/login/')
        
        
    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'username  invalid')
            return redirect('/auth_practice/login/')
        
        user = authenticate(username = username, password = password)
        if(user):
            login(request, user)
            return redirect('/auth_practice')
        else:
            messages.error(request, ' password invalid')
            return redirect('/auth_practice/login/')


    return render(request, 'login.html')

def signout(req):
    logout(req)
    return redirect('/auth_practice/login')