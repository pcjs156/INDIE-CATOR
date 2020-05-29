from django.shortcuts import render, redirect
from .forms import SignInForm, SignUpForm
from django.urls.base import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_check'] :
                new_user = form.save()
                return redirect('/event/')
    else :
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        ID = request.POST['username']
        PW = request.POST['password']
        u = authenticate(username=ID, password=PW)

        if u:
            login(request, user=u)
            return redirect('/event/')
        else :
            return render(request, 'signin.html', {'form':form, 'error':'아이디 또는 비밀번호가 일치하지 않습니다.'})
    
    else :
        form = SignInForm()
        return render(request, 'signin.html', {'form':form})
       
def signout(request):
    logout(request)
    return redirect('/event/')