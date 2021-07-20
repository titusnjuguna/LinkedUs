from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from PIL import Image

# Create your models here.
class Jobs(models.Model):
    job_id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    experience = models.CharField(max_length=30,null=True , blank=True)
    summary = RichTextField(max_length = 150,null=True,blank=True)
    description= RichTextField(max_length=2000,null=True,blank=True)
    author = models.ForeignKey(User ,null=True,blank=True,on_delete = models.CASCADE)
    salary = models.DecimalField(max_digits=10,null=True,blank=True,decimal_places=0)
    location = models.CharField(max_length=30,null=True,blank=True )
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('Job-detail',kwargs={'pk':self.pk})    