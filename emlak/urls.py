from django.conf.urls import url
from .views import *


app_name = 'emlak'

urlpatterns = [

    url(r'^kiralik/$', emlak_index_kiralik, name='kiralik'),
    url(r'^satilik/$', emlak_index_satilik, name='satilik'),
    url(r'^create/$', emlak_create, name='create'),
    url(r'^(?P<id>\d+).html$', emlak_detail, name='detail'),
    url(r'^(?P<id>\d+)/update/$', emlak_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', emlak_delete, name='delete'),
]

