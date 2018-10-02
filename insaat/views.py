from django.shortcuts import render
from .models import Insaat


def hakkimizda_view(request):
    firma = Insaat.objects.get(id=1)
    return render(request, 'hakkimizda.html', {'firma': firma})

def iletisim_view(request):
    firma = Insaat.objects.get(id=1)
    return render(request, 'iletisim.html', {'firma': firma})
