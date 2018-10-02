from django.conf.urls import url
from .views import *

app_name = 'proje'

urlpatterns = [

    url(r'^index/$', proje_index, name='index'),
    url(r'^create/$', proje_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/(?P<id>\d+)/$', proje_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', proje_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', proje_delete, name='delete'),
]
