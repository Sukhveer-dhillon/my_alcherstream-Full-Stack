# automatically creates profile when user registers
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# django signals(when user is created call create profile)
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

# django signals(when user is saved call save profile)
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()

# then in apps.py file add this file
    