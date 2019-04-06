from django.shortcuts import render
from . import models
from django.http import HttpResponse
# Create your views here.


def post_list(request):
    posts = models.Post.objects.all()
    return render(request, "posts/post_list.html", {'posts': posts})


def post_detail(request, slug):
    #return HttpResponse(slug)
    post = models.Post.objects.get(slug = slug)
    return render(request, 'posts/post_detail.html', {'post': post})

