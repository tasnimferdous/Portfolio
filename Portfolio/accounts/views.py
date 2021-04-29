from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request, user)
            messages.info(request, 'Logged in')
            return redirect('/')
        else:
            messages.info(request, 'Invaliud credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, email = email, password = password1)
                user.save()
                messages.info(request, 'Account created')
                return redirect('login')
        else:
            messages.info(request, 'Password is not matching')
            return redirect('register')
    else:    
        return render(request, 'register.html')




# -----------------------



