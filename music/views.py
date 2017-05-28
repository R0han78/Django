from django.views import generic
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums' #to change name object_list to all_albums
    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

    
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class AlbumCreate(CreateView):
    model = Album
    fields=['artist','album_title']

    
class AlbumUpdate(UpdateView):
    model = Album
    fields=['artist','album_title']
    
    
from django.core.urlresolvers import reverse_lazy
class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')