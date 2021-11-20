from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import request, HttpResponse
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CompRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account crearted successful')
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
            return redirect('Profile_Page')

    else:
        u_form = CompUpdateForm(instance=request.user)
        p_form = ProfilePicForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'Users/profile.html', context)
