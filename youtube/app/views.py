from django.shortcuts import render
from models import *
from django.http import *
from pytube import YouTube
from wsgiref.util import FileWrapper
from django.conf import settings

# not necessary, just for demo purposes.
from pprint import pprint

# Create your views here.

def home(request):

	return render(request,'home.html')

def download(request):
	link=request.POST['link']
	query=Video(link=link) 
	query.save()
	
	yt = YouTube(link)
	pprint(yt.get_videos())
	print(yt.filename)
	
	yt.set_filename(yt.filename)
	pprint(yt.filter('flv'))
	print(yt.filter('mp4')[-1])
	pprint(yt.filter(resolution='480p'))

	video = yt.get('mp4', '360p') 
	video.download(settings.STATIC_ROOT+'/')
	return HttpResponse("HHH");
	return HttpResponseRedirect('/hell.mp4')

	