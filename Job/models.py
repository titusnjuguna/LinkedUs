from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.urls import reverse
#from PIL import Image


# Create your models here.
class Jobs(models.Model):
    #id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    experience = models.CharField(max_length=30, null=True, blank=True)
    description = RichTextField(max_length=2000, null=True, blank=True)
    salary = models.DecimalField(
        max_digits=10, null=True, blank=True, decimal_places=0)
    location = models.CharField(max_length=30, null=True, blank=True)
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

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
    company = models.ManyToManyField(Jobs, blank=True)

    def __str__(self):
        return str(self.name)
