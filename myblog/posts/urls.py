from django.conf.urls import url
from django.urls import path
from posts.views import post_list,post_detail,new_post

urlpatterns=[
    url('^$',post_list,name='post_list'),
    path('posts/<int:pk>/',post_detail,name='post_detail'),
    path('posts/new/',new_post,name='new_post')

]