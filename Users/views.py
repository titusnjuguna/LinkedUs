from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate
from rest_framework import  viewsets,permissions
from django.http import request , HttpResponse
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login,logout,authenticate


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CompRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('Login')
    else:
        form = CompRegisterForm()
    return render(request, 'Users/register.html', {'form': form})      




@login_required
def profile(request):
    if request.method == 'POST':
        u_form = CompUpdateForm(request.POST, instance=request.user)
        p_form = ProfilePicForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = CompUpdateForm(instance=request.user)
        p_form = ProfilePicForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'Users/profile.html', context)        