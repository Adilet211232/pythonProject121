from  django.http import  HttpResponse
from django.shortcuts import render
from  . import  models
def hello_world(request):
        return HttpResponse('Hello world')

def kniga_all(request):
        post = models.Post.objects.all()
        return  render(request, 'post_list.html',{'post':post})