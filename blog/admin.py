from django.contrib import admin

# Register your models here.
# post is imported for putting it in admin page alongside users and group 
from .models import Post

admin.site.register(Post)
