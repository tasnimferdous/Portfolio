from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from accounts.views import login

def template(request):
    return render(request, 'template.html')

def form(request):
    if request.user.is_authenticated:
        return render(request, 'form.html')
    else:
        return redirect('login')
