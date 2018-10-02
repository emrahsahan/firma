from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Blog
from .models import Blogresim
from .forms import BlogForm
from django.utils.text import slugify
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def post_index(request):
    post_list = Blog.objects.filter(aktif=True)
    paginator = Paginator(post_list, 4)
    sayfa = request.GET.get('sayfa')
    posts = paginator.get_page(sayfa)
    return render(request, 'haber/index.html', {'posts': posts})

def post_detail(request, slug, id):
    post = get_object_or_404(Blog, slug=slug, aktif=True)

    return render(request, 'haber/detail.html', {'post': post,})

def post_create(request):

    if not request.user.is_authenticated:
        return redirect('post:index')


    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'haber/form.html', context)

def post_update(request, slug):

    if not request.user.is_authenticated:
        return redirect('post:index')

    post = get_object_or_404(Blog, slug=slug)
    form = BlogForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'haber/form.html', context)

def post_delete(request, slug):

    if not request.user.is_authenticated:
        return redirect('post:index')

    post = get_object_or_404(Blog, slug=slug)
    post.delete()
    return redirect('post:index')

