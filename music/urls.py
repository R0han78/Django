from django.conf.urls import url
from django.contrib import admin
from .import views

app_name = 'music'

urlpatterns = [
#    #/music/
#    url(r'^$', views.index , name='index'),
#    
#    #music/<album_id>/
#    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
    
#    #music/<album_id>/favourite/
#    url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite,name='favourite'),
    
    #/music/
    url(r'^$', views.IndexView.as_view() , name='index'),
    
    #music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),name='detail'),
    
    #/music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(),name='album-add'),
    
    #/music/album/<album_id>
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(),name='album-update'),
    
    #/music/album/<album_id>/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(),name='album-delete'),
]




