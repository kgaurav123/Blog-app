from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render,HttpResponse
from.models import Contact
from Blog.models import Post
# Create your views here.
def home(request):
    allposts=Post.objects.all()[:3]
    context={'allposts':allposts}
    return render(request,'home/home.html',context)
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email)<6 or len(phone)<10 or len(content)<10:
            messages.error(request,'Please fill the form correctly')
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Your messages have been sent successfully')
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')
def search(request):
    query=request.GET['query']
    if len(query)>78:
        allposts = Post.objects.none()
    else:
        allpostsTitle = Post.objects.filter(title__icontains=query)
        allpostsContent = Post.objects.filter(content__icontains=query)
        allpostsAuthor = Post.objects.filter(author__icontains=query)
        allpoststimestamp = Post.objects.filter(timestamp__icontains=query)
        allposts=allpostsTitle.union(allpostsContent, allpostsAuthor, allpoststimestamp)
    if allposts.count() == 0:
        messages.error(request,'No such result found,please refine your search')
    params={'allposts':allposts,'query':query}
    return render(request,'home/search.html',params)