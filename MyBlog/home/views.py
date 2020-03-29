from django.shortcuts import render,HttpResponse
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'home/home.html')
def about(request):
    return render(request,'home/about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']

        if len(name)<3 or len(email)<6 or len(phone)!=10 or len(content)<6:
            messages.error(request,"Please Fill the form correctly")
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your Response was succesfully submitted")

    return render(request,'home/contact.html')
def slug1(request, slug):
    return render(request,'slug.html')