from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method=="POST":
        if request.POST['password1']==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create(username=request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',{'error':'Password Not Match'})
    
    return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html' ,{'error':'username or password is incorrect.'})        
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')