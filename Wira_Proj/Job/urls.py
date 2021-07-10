from django.urls import path
from . import views
from .views import  JobCreateView

urlpatterns = [
    path('', views.home,name='Job-home'),
    path('Job/New/',JobCreateView.as_view(), name='Job-create'),
           ]