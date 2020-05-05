from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def contact(request):
    return render(request,'home/contact.html')

