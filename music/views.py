# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,Http404
from .models import Album

# Create your views here.

#type 1
#def index(request):
#    all_albums = Album.objects.all()
#    html=''
#    for album in all_albums:
#        url = '/music/'+str(album.id)+'/'
#        html+='<a href="'+url+'">'+album.album_title+'</a><br>'
#    return HttpResponse(html)


#type 2
#from django.template import loader
#def index(request):
#    all_albums = Album.objects.all()
#    template = loader.get_template('music/index.html')
#    context = {
#        'all_albums' : all_albums,
#    }
#    return HttpResponse(template.render(context,request))


#type3
from django.shortcuts import render
def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums' : all_albums,
    }
    return render(request,'music/index.html',context)





#type 1
#def detail(request,album_id):
#    try:
#        album = Album.objects.get(pk=album_id)
#    except Album.DoesNotExist:
#        raise Http404("Album Not Present")
#    context = {
#        'album' : album,
#    }
#    return render(request,'music/details.html',context)
#

#type 2
from django.shortcuts import get_object_or_404
def detail(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    context = {
        'album' : album,
    }
    return render(request,'music/details.html',context)





