from django.shortcuts import render
from .models import Temizlik
# Create your views here.

def temizlik_view(request):
    temizlik = Temizlik.objects.get(id=1)
    return render(request, 'temizlik.html', {'temizlik': temizlik})

def bina_view(request):
    bina = Temizlik.objects.get(id=2)
    return render(request, 'bina.html', {'bina': bina})