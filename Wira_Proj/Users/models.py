from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
   
    #USER_CATEGORY =[(EMPLOYER,'employer'),(JOB_SEEKER,'Job_seeker')]
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    image= models.ImageField(default='default.jpg', upload_to='profile_pics')
    #account_type = models.CharField(max_length=2,choices=USER_CATEGORY,default = JOB_SEEKER)



    def __str__(self):
        return f'{self.user.username}profile'
        
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 200 and img.width > 200:
            output_size=(150,150)
            img.thumbnail(output_size)
            img.save(self.image.path)    