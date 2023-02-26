from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.(acts as request handler) takes request -> response
from .models import VideoSubtitle
# from .forms import VideoForm


# def showvideo(request):
#     lastvideo = VideoSubtitle_video.objects.last()
#
#     videofile = lastvideo.videofile
#
#     form = VideoForm(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#
#     context = {'videofile': videofile,
#                'form': form
#                }
#
#     return render(request, 'videos.html', context)


def say_hello(request):
    x = calculate()
    return render(request, 'hello.html', {'name': 'Ram', 'x': x}) #return HttpResponse('Hello Meghana')


def calculate():
    x=1
    y=2
    return x+y


def index(request):
    video= VideoSubtitle.objects.all()
    return render(request, "videos.html", {"video": video})