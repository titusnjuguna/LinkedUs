from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CompRegisterForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class CompUpdateForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']     

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']            