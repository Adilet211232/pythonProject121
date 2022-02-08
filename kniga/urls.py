
from django.urls import path , include
from . import  views

urlpatterns = [
    path('hello/', views.hello_world, name = 'hello'),
    path('posts/', views.kniga_all, name = 'posts'),
]

