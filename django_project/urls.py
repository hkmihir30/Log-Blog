# QUERY 

"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# this is another way for accessing urls directly from views 
# Instead of making urls in users and then adding in urlpatterns 
from users import views as user_views

# imported for login logout and password reset as well
# LoginView, LogoutView and PasswordResetView
from django.contrib.auth import views as auth_views

# this is from the django documentation related to saving things entered from the user 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register,name='register'),
    path('profile/', user_views.profile,name='profile'),

    # If you’re only changing a few attributes on a class-based view,
    #  you can pass them into the as_view() method call itself
    # these enables to direct us to templates made by us 
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),

    # this route is for changing the password 
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),

    # this route is for the message sent on successfully sending the email to change the password
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),

    # this route is for password_reset_confirm the error we had seen while changing the password 
    # uidb64 is for the user encoded in 64 bit
    # token is for whether the password is same or not 
    # these parametres need to be put as it ask for them to be there 
    # and without them error will be there  
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),

    # this is for the successful completion of the password change
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
        
    path('', include('blog.urls'))
]


# this is edited from the django documentation related to saving things entered from the user 
# QUERY : only add that when we are in the Debug mode but why 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
