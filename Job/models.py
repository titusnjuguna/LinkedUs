from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.urls import reverse
#from PIL import Image


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(
            PublishedManager, self
        ).get_queryset()\
            .filter(status='published')

# Create your models here.
class Jobs(models.Model):
    published = PublishedManager()
    title = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    salary = models.DecimalField(
        max_digits=10, null=True, blank=True, decimal_places=0)
    location = models.CharField(max_length=30, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now = True)

    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('Job-detail', kwargs={'pk': self.pk})


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
    

    def __str__(self):
        return str(self.name)
