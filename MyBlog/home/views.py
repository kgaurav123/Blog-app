from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
# Create your views here.
from django.shortcuts import render,HttpResponse,redirect
from.models import Contact
from Blog.models import Post
from django.contrib.auth import authenticate,login, logout
# Create your views here.
def home(request):
    allposts=Post.objects.all()[:2]
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

def handlesignup(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        #check for erroneous inputs
        if len(username) > 15:
            messages.error(request,'Your username should be under 10 characters')
            return redirect('handlesignup')
        
        if not username.isalnum():
            messages.error(request,'Username should only consists of alphabets and number')
            return redirect('handlesignup')
            
        if pass1 != pass2:
            messages.error(request,'Passwords do not match')
            return redirect('handlesignup')

        #create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Your account has been successfully created,Login here')
        return redirect('handlesignup')
    else:
        return render(request,'home/signup.html')
    
        
    
def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        
        user = authenticate(username=loginusername,password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request,'Successfully logged in')
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('handlelogin')
    return render(request,'home/login.html') 
        
def handlelogout(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect('home')
    return HttpResponse('logout')
    