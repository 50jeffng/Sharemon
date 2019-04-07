from django.shortcuts import render
from . import models
from django.http import HttpResponse
# Create your views here.


def post_list(request):
    posts = models.Post.objects.all()
    return render(request, "html/request.html", {'posts': posts})


def event_list(request):
    events = models.Event.objects.all()
    return render(request, "html/event.html", {'events': events})


def post_detail(request, slug):
    #return HttpResponse(slug)
    post = models.Post.objects.get(slug = slug)
    return render(request, 'html/request_details.html', {'post': post})

def event_detail(request, slug):
    #return HttpResponse(slug)
    event = models.Event.objects.get(slug = slug)
    return render(request, 'html/event_details.html', {'event': event})

