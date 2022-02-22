from email import message
from urllib import response
from urllib.request import Request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'manage_user/login.html')



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created!')
            return redirect('login')
        else:
            username=form.cleaned_data.get('username')
            messages.success(request, f'Invalid Input!')
            return render(request, 'manage_user/register.html' , {'form':form})
    else:
        form = UserRegistrationForm()
    
    return render(request, 'manage_user/register.html' , {'form':form})


@login_required
def profile(request):
    return render(request, 'manage_user/profile.html')
    
