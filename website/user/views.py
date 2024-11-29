from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import user
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'GET':
        form = UserRegistrationForm()
        return render(request, 'index.html', {'form': form})


    elif request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = user.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            messages.success(request, 'Registration successful!')
            return redirect('')
   
