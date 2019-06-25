from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
# Create your views here.


def success(request):
    return render(request, 'accounts/success.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return render(request, 'accounts/success.html')
        else:
             return HttpResponse("Password doesn't match. Please re-enter.")
    return render(request, 'accounts/signup.html')


def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                return HttpResponse("ID or Password do not match. Please re-enter.")
        else:
            return render(request, 'accounts/login.html')
            
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('blog')
    return render(request, 'accounts/login.html')

