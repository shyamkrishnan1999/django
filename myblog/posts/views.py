from django.shortcuts import render
from posts.models import Post

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(is_active=True)
    return render(request,'post/post_list.html',{"posts":posts})

def post_detail(request,pk):
    post=Post.objects.get(id=pk)
    return render(request,'post/post_detail.html',{"post":post})

