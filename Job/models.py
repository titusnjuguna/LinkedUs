from email.mime import application
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from Users.models import Profile



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

# Create your models here.
class Candidates(models.Model):
    category = (
        ('Male', 'male'),
        ('Female', 'female'),
        ('Other', 'other'),
    )
    name = models.CharField(max_length=200, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=200, null=True, choices=category)
    mobile = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    resume = models.FileField(null=True)
    cover = models.TextField()
       
    def __str__(self):
        return str(self.name)

class Jobs(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    #renaming model manager
    published = PublishedManager()
    title = models.CharField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(Profile,on_delete= models.CASCADE, related_name='job_Author')
    experience = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    Responsibility = models.TextField(max_length=2000, null=True, blank=True)
    qualification = models.TextField(max_length=2000, null=True, blank=True)
    job_type = models.CharField(max_length=30, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=0)
    total_opening = models.DecimalField(max_digits=100,null=True, blank=True, decimal_places=0)
    location = models.CharField(max_length=30, null=True, blank=True)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now = True)
    status =  models.CharField(max_length=15,default='draft',choices= STATUS_CHOICES)
    applicants = models.ManyToManyField(Candidates)
     
    
    class Meta:
        ordering = ('-publish',)
   
    def __str__(self):
        return str(self.title)
              
    def get_absolute_url(self):
        return reverse('Job:Job-detail',
        args=[self.publish.year,self.publish.month,self.publish.day, self.slug])
