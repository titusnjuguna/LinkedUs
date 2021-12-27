from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class SearchForm(forms.Form):
    title= forms.CharField(max_length=30,label="title")
    location = forms.CharField(max_length=30,label="Location")
    experience = forms.CharField(max_length=30,label="Experience")
    

class JobCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea ,label="Job_Description")
    location = forms.CharField(label="Location",widget=forms.Select(choices='Job_Location'))
    salary = forms.DecimalField(label="salary")
    experience = forms.CharField(max_length=30, label="Experience")
    industry = forms.CharField(label="Industry", widget = forms.Select(choices='Job_industry'))

class ApplyForm(forms.ModelForm):
    #dob = forms.DateField( widget=forms.DateInput(format='%d-%m-%Y'),
    #    input_formats=['%d-%m-%Y'])
    class Meta:
        model = Candidates  
        exclude = ['dob']
  

