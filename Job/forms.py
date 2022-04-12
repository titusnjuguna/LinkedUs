from operator import index
from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from .models import *

class SearchForm(forms.Form):
    title= forms.CharField(max_length=30,label="title")
    location = forms.CharField(max_length=30,label="Location")
    experience = forms.CharField(max_length=30,label="Experience")
    
class JobCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea ,label="Job_Description")
    location = forms.CharField(label="Location")
    salary = forms.DecimalField(label="salary")
    experience = forms.CharField(max_length=30, label="Experience")
    industry = forms.CharField(label="Industry")
    Responsibility = forms.Textarea()
    qualification = forms.Textarea()
    job_type = forms.CharField(label="Job_type")
    total_opening =forms.DecimalField(label='total_opening')
    
        
    

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Candidates  
        exclude = ['dob']
  

