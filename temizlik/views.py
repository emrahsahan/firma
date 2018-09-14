from django.shortcuts import render
from .models import Temizlik
# Create your views here.

def temizlik_view(request):
    temizlik = Temizlik.objects.get(id=1)
    return render(request, 'temizlik.html', {'temizlik': temizlik})