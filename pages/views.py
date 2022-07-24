from django.shortcuts import render
from blogpart.models import Post
# Create your views here.
def home(request,*args,**kwargs):
    return render(request,"index.html",{})
def blogposts(request,*args,**kwargs):
    posts=Post.objects.all()
    return render(request,"blogs.html",{"posts":posts})
