from django.shortcuts import render, HttpResponse, redirect
from haber.models import Blog
from emlak.models import Emlak
from proje.models import Proje
from django.db.models import Count

# Create your views here.
def home_view(request):
    posts = Blog.objects.all()[:3]
    kiralik_list = Emlak.objects.filter(aktif=True, durum='2')[:9]
    satilik_list = Emlak.objects.filter(aktif=True, durum='1')[:9]
    proje_list = Proje.objects.all()[:4]

    return render(request, 'home.html', {'posts': posts,
                                         'kiralik_list': kiralik_list,
                                         'satilik_list': satilik_list,
                                         'proje_list': proje_list})