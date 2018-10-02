from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Emlak
from .forms import EmlakForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import EmlakFoto
from django.db.models import Q


# Create your views here.
def emlak_index_kiralik(request):
    emlak_list = Emlak.objects.filter(aktif=True, durum='2')

    query = request.GET.get('q')

    if query:
        emlak_list = emlak_list.filter(Q(mahalle__icontains=query) |
                                       Q(ilce__icontains=query) |
                                       Q(il__icontains=query) |
                                       Q(oda__icontains=query) |
                                       Q(buyukluk__icontains=query)).distinct()

    paginator = Paginator(emlak_list, 6)
    sayfa = request.GET.get('sayfa')
    emlaks = paginator.get_page(sayfa)
    return render(request, 'emlak/kiralik.html', {'emlaks': emlaks})

def emlak_index_satilik(request):
    emlak_list = Emlak.objects.filter(aktif=True, durum='1')

    query = request.GET.get('q')
    if query:
        emlak_list = emlak_list.filter(Q(mahalle__icontains=query) |
                                       Q(ilce__icontains=query) |
                                       Q(il__icontains=query) |
                                       Q(oda__icontains=query) |
                                       Q(buyukluk__icontains=query)).distinct()

    paginator = Paginator(emlak_list, 6)
    sayfa = request.GET.get('sayfa')
    emlaks = paginator.get_page(sayfa)
    return render(request, 'emlak/satilik.html', {'emlaks': emlaks})

def emlak_detail(request, id):
    emlak = get_object_or_404(Emlak, id=id, aktif=True)

    return render(request, 'emlak/detail.html', {'emlak': emlak, })

def emlak_create(request):

    if not request.user.is_authenticated:
        return redirect('emlak:kiralik')


    form = EmlakForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        emlak = form.save()
        return HttpResponseRedirect(emlak.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'emlak/form.html', context)

def emlak_update(request, id):

    if not request.user.is_authenticated:
        return redirect('emlak:kiralik')

    emlak= get_object_or_404(Emlak, id=id)
    form = EmlakForm(request.POST or None, request.FILES or None, instance=emlak)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(emlak.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request, 'emlak/form.html', context)

def emlak_delete(request, id):

    if not request.user.is_authenticated:
        return redirect('emlak:kiralik')

    emlak = get_object_or_404(Emlak, id=id)
    emlak.delete()
    return redirect('emlak:kiralik')