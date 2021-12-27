from django.contrib.auth.models import User,Group
from django.db.models.base import Model
from .models import  Jobs as JobsModel
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields = ['username','groups','date_joined']


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= JobsModel
        fields = ['title','experience','location','salary']        
        
