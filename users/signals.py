# this has been created for automatically creating profiles for every new user created 

# this has been included to run this post_save signal as a user creates his/her account 
from django.db.models.signals import post_save

# this will be sending the signal 
from django.contrib.auth.models import User

# this receiver will be receiving the signals and performing some tasks 
from django.dispatch import receiver

from .models import Profile

# here we have used kwargs only for all other arguements 
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
    instance.profile.save()