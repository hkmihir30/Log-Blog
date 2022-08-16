from django.db import models
from django.contrib.auth.models import User

# this is pillow library for images
from PIL import Image


class Profile(models.Model):

    # user is here our user (the one who has profile)
    # Onetoonefield establish one to one relation  
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # profile_pics is the directory where profile pics get uploaded 
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    # these dunder methods are used for specifying what to show 
    # here on showing profile it also shows "username profile"
    def __str__(self):
        return f'{self.user.username} Profile'

    # this save is already present in the parent class and it runs after our model is saved
    # we also need to have the parametres that this save function might be accepting 
    def save(self,*args, **kwargs):
        
        # we run the save() function of its parent class
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        # we are doing this to reduce the space it is taking 
        # and then the browser also runs slowly , so to speed up that also 
        if img.height > 300 or img.width > 300 :
            output_size = (300,300)

            # this resizes the image 
            img.thumbnail(output_size)

            img.save(self.image.path)

    

