from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse
from.models import Contact
# Create your views here.
def home(request):
    return render(request,'home/home.html')
def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        contact = Contact(name=name,email=email,phone=phone,content=content)
        contact.save()
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')