from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Proje
from .forms import ProjeForm
from django.utils.text import slugify

# Create your views here.

def proje_index(request):
    projes = Proje.objects.all()
    return render(request, 'proje/index.html', {'projes': projes})

def proje_detail(request, slug, id):
    proje = get_object_or_404(Proje, slug=slug)
    return render(request, 'proje/detail.html', {'proje': proje})

def proje_create(request):

    if not request.user.is_authenticated:
        return redirect('proje:index')


    form = ProjeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        proje = form.save()
        return HttpResponseRedirect(proje.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'proje/form.html', context)

def proje_update(request, slug):

    if not request.user.is_authenticated:
        return redirect('proje:index')

    proje = get_object_or_404(Proje, slug=slug)
    form = ProjeForm(request.POST or None, request.FILES or None, instance=proje)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(proje.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'proje/form.html', context)

def proje_delete(request, slug):

    if not request.user.is_authenticated:
        return redirect('proje:index')

    proje = get_object_or_404(Proje, slug=slug)
    proje.delete()
    return redirect('proje:index')