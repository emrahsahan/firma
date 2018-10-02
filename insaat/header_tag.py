from django import template
from insaat.models import Insaat

def header_get(request):
    data = Insaat.objects.get(id=1)
    return {'data': data}
