from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.blogHome,name='blogHome'),
    path('post',views.blogPost,name='blogPost'),
    path('<str:slug>',views.slug2,name='slug2'),
]