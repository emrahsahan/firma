from django.shortcuts import render, HttpResponse
from haber.models import Blog

from django.db.models import Count
# Create your views here.
def home_view(request):
    posts = Blog.objects.all()[:3]
    return render(request, 'home.html', {'posts': posts})

