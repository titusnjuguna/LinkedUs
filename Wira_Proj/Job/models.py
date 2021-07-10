from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Jobs(models.Model):
    job_id= models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,null=True,blank=True)
    experience = models.CharField(max_length=30,null=True , blank=True)
    description= models.TextField(max_length=1000,null=True,blank=True)
    employer = models.ForeignKey(User,null=True,blank=True ,on_delete = models.CASCADE)
    salary = models.DecimalField(max_digits=10,null=True,blank=True , decimal_places=0)
    location = models.CharField(max_length=30,null=True,blank=True )
    date_posted = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title 