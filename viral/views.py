from django.http import request
from django.shortcuts import render, redirect
from pytube import YouTube
from django.contrib import messages
from django.http import FileResponse
# Create your views here.
video_url = ""


def downl(request):
    return render(request, 'home.html')


def lint(request):

    if(request.method == "POST"):
        global video_url
        video_url = request.POST['url']
        print(video_url)
        yt = YouTube(video_url)
        x = yt.title
        y = yt.description
        embed_link = video_url.replace("watch?v=", "embed/")
        return render(request, 'completed.html', {'title': x, 'description': y, 'embd': embed_link})


def song(request):
    global video_url
    print(video_url)
    x = "Mp3"
    return FileResponse(open(YouTube(video_url).streams.filter(only_audio=True).first().download(skip_existing=True), 'rb'))


def video(request):
    global video_url
    print(video_url)
    x = "Video"
    return FileResponse(open(YouTube(video_url).streams.filter(only_video=True).first().download(skip_existing=True), 'rb'))
