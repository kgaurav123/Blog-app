from django.shortcuts import render,HttpResponse
from .models import Post
# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}
    return render(request,'blog/blogHome.html', context)
def blogPost(request):
    return render(request,'blog/blogpost.html')
def slug2(request, slug):
    return render(request,'slug.html')
