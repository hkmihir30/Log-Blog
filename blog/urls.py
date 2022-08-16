from django.urls import path

# imported for using class bases views here 
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)

from . import views

urlpatterns = [
    # Here putting '' means homepage 
    # this was used earlier 
    # path('', views.home ,name = 'blog-home'),

    # now this is used as a class based views 
    # to use class based views we need to convert the class in views form 
    # for this as_view() function is used 
    path('', PostListView.as_view() ,name = 'blog-home'),

    # this one is for all the posts of a particular user 
    path('user/<str:username>', UserPostListView.as_view() ,name = 'user-posts'),

    # the first argument signifies the use of variable in url patter which django provides 
    # like a post have pk - primary key 1 then it will be like post/1/ 
    # int: signifies that only take int argument 
    # detailview accepts pk as variable by default 
    # we can change this 'pk' name in class although no need is there 
    path('post/<int:pk>/', PostDetailView.as_view() ,name = 'post-detail'),

    path('post/new/', PostCreateView.as_view() ,name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() ,name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() ,name = 'post-delete'),
    
    # Here putting about in path means that you will have to put in search bar for seeking it 
    path('about/', views.about ,name = 'blog-about'),
]