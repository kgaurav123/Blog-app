from django.shortcuts import render,HttpResponse
from.models import Post
# Create your views here.
def index(request):
    allposts = Post.objects.all()
    context = {'allposts':allposts}
    return render(request,'blog/index.html', context)
def blogpost(request,slug):
    post=Post.objects.filter(slug=slug)[0]
    print(post)
    context={'post':post}
    return render(request,'blog/blogpost.html',context)