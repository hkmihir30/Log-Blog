from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# imported in order to update it 
# It doesn't reside in the User model 
from .models import Profile

# this class is inherited from usercreationform 
# It add extra features of email 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


# this is added to update userrname and email 
# it has all the classes of forms.ModelForm as it is inherited from that 
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

# additional class added to update profile_pic 
# since it is in the profile model (not same as the user model)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']