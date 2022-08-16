# This is imported to include the html code 
# written for a def like home here 
# get_object_or_404 imported for giving error if the user doesn't exit 
# in the case when we are opening his/her posts 
from django.shortcuts import( 
    render,
    get_object_or_404
) 

# imported for the pagination of the posts written by a particular user 
from django.contrib.auth.models import User

# imported for asking to login if we want to create a post without logging in 
# we need to inherit classes for which to use it 
# we shall put in the left only 
# Userpassestestmixin imported so that you can't edit someone's else post
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

# .models is used since it is also in the same directory
from .models import Post

# This was earlier used for httpresponse
# from django.http import HttpResponse

# imported for making home a class based list view 
# And then for the detailview of a single post 
# Createview to create a post 
# Updateview to update a post 
# Deleteview to delete a post 
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# imported for redirecting to home using success_url after creating a post 
from django.urls import reverse,reverse_lazy

# this is the earlier used dummy data
# posts=[
#     {
        # 'author''Mihir',
#         'title':'Blog post 1',
#         'content':'first post content',
#         'date_posted':'feb15,2021',
#     },
#     {
#         'author':'Hooku',
#         'title':'Blog post 2',
#         'content':'second post content',
#         'date_posted':'Aug18,2021',
#     }
# ]

# this is a function based views 
def home(request):
    
    # this is the way to access this in the template (also used in users views)
    context = {
        'posts' : Post.objects.all()
    }   

    # render returns a http response or an exception 
    # Firt argument is request itself , while 2nd is path
    # to html file including the subdirectory where it resides
    return render(request,'blog/home.html',context)

# this is a class based views 
class PostListView(ListView):
    
    # this is the model we want to query to create the list (here Post) 
    model = Post

    # this is done to change the template from the default "blog/post_list.html" to this
    # Or we could make one template with that name ... which is cumbersome 
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html

    # by default context_object_name is object_list 
    # so either we change it in the template or just change the name here back to 'posts'
    context_object_name = 'posts'

    # this ordering attribute checks for the order in which query is made to database
    # -date_posted (minus)date_posted means show it from latest to oldest  
    ordering = ['-date_posted']

    paginate_by = 5

class UserPostListView(ListView):
     
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


# this is a class based views 
class PostDetailView(DetailView):
    
    # this is the model we want to query to create the list (here Post) 
    model = Post

# LoginRequiredMixin put in left due to some sort of inheritance property to work 
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    #here we have override the form_valid function 
    def form_valid(self,form):

        #here we changed the author to the current logged in user  
        form.instance.author = self.request.user
        return super().form_valid(form)

    # to go on the homepage after creating post this line is needed 
    # we can't use reverse with success_url , reverse_lazy is used 
    # success_url = reverse_lazy('blog-home')

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    #here we have override the form_valid function 
    def form_valid(self,form):

        #here we changed the author to the current logged in user  
        form.instance.author = self.request.user
        return super().form_valid(form)

    # this function is run bu userpasses... in order to see if
    # user passes a test condition 
    def test_func(self):

        # get_object() is a method of Updateview which gives the post that we are trying to update 
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else :
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    
    # this is the model we want to query to create the list (here Post) 
    model = Post

    # success_url just takes the path where we want to go after the command is processed 
    success_url = '/'
    # the following line will do the same work as the above one 
    # success_url = reverse_lazy('blog-home')

    def test_func(self):

        # get_object() is a method of Updateview which gives the post that we are trying to update 
        post = self.get_object()

        if self.request.user == post.author:
            return True
        else :
            return False

    

# this is a function based views 
def about(request):

    # title = {
    #     'title':'About'
    # }
    # return render(request,'blog/about.html',title)

    # The above commented code is equivalent
    #  to the one written down in whick we can directly pass
    # the dictionary
    return render(request,'blog/about.html',{'title':'About'})

    # Basic way of returning httpresponce
    # return HttpResponse('<h1>Blog About</h1>')

 
