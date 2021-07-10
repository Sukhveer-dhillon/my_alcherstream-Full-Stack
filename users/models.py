from django.db import models

# Create your models here.
# extending existing user model of django to add profile pic
from django.contrib.auth.models import User
# Create your models here.
# for profile image size
from PIL import Image

class Profile(models.Model):
    # cascade means if user is deleted delete profile also
    # one to one means one profile pic per user
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.png', upload_to='profile_pics')

    # how it will be printed
    def __str__(self):
        return f'{self.user.username} Profile'
    
    # for profile image size
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        # will get current user image
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
