from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# imported for redirecting to blogdetail after creating a post 
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # default datetime also set here 
    date_posted = models.DateTimeField(default=timezone.now)

    # this makes the author as the user who created the post 
    # on_delete= models.CASCADE is used for when the user is deleted
    # then the post made by him should also be deleted but not the other way round
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    
    # these dunder methods are used for specifying what to show
    def __str__(self):
        return self.title

    # this is run for any specific instance of a post 
    # here used for redirecting us to detail section after creating a post 
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    

    

    

    
    