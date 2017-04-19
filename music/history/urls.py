from django.conf.urls import url

from . import views

app_name = 'history'
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    # To list all artists
    url(r'^$', views.ListView.as_view(), name='list'),
    # To show specific details on a given artist
    url(r'^(?P<pk>[0-9]+)/detail/$', views.DetailView.as_view(), name='detail')
]    
