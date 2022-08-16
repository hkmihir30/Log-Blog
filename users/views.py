from django.shortcuts import render,redirect

# django already has form inbuilt which we had imported earlier
# Now we are inheriting it in self made userregisterform 
# which has some extra attributes  
from django.contrib.auth.forms import UserCreationForm

# imported for alert message 
from django.contrib import messages

# imported for decorator restricting access to profile when not logged in 
from django.contrib.auth.decorators import login_required

# This is new form inherited from usercreationform in forms.py file 
# the same is about others also 
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm



def register(request):
    if request.method == 'POST':

        # here form taked the data given as argument
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            # for saving the newuser else nothing will be saved
            form.save()

            # cleaned_data gives all the validated data 
            username = form.cleaned_data.get('username')

            # earlier - gives message when it is a success
            # messages.success(request,f"Account created for {username}!")

            # this redirects to home page after the form is submitted 
            # return redirect('blog-home')

            #now
            messages.success(request,f"Your account has been created! You can now login")
            
            # this redirects to login page so the user may login 
            return redirect('login')
    else :

        # here the form created is empty
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

# decorator used to restrict from the profile access when the user isn't logged in
# later on we added login-url = 'login' in setting.py for redirecting us to login page to view profile 
@login_required 
def profile(request):
    if request.method == 'POST':

        # the first argument here is the new_data going to be passed 
        # while the last argument is the data to be initially shown before updating 
        u_form = UserUpdateForm(request.POST,instance=request.user)

        # request.FILES is needed for the images 
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Your account has been updated!")
            return redirect('profile')
    else :
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form 
    }

    return render(request, 'users/profile.html', context)