from django.contrib import admin

# imported for making users to be seen on admin page
from .models import Profile 

# this is the way to register something
admin.site.register(Profile)
