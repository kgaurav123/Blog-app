from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(request):
    return render(request,'blog/blogHome.html')
def blogPost(request):
    return render(request,'blog/blogpost.html')
def slug2(request, slug):
    return render(request,'slug.html')
