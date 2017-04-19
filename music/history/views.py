from django.views import generic
from .models import Artist


class ListView(generic.ListView):
    # Shows a list of available artists
    context_object_name = "artist_list"
    model = Artist
    template_name = 'history/list.html'

class DetailView(generic.DetailView):
    model = Artist
    template_name = 'history/detail.html'
