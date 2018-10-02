from django.contrib import admin
from .models import Proje
from .models import Projefoto
from .models import Daire
# Register your models here.

class ProjeAdmin(admin.ModelAdmin):

    list_display = ['projeadi', 'resim', 'tarih', 'slug']
    list_filter = ['projeadi']
    search_fields = ['projeadi']

    class Meta:
        model = Proje

class ProjefotoAdmin(admin.ModelAdmin):

    list_display = ['proje', 'fotograf']
    list_filter = ['proje']
    search_fields = ['proje__projeadi']

    class Meta:
        model = Projefoto

class DaireAdmin(admin.ModelAdmin):

    list_display = ['proje', 'daireno', 'kat', 'blok', 'alan', 'satis']
    list_display_links = ['proje', 'daireno']
    list_filter = ['proje']
    search_fields = ['proje__projeadi']

    class Meta:
        model = Daire

admin.site.register(Proje, ProjeAdmin)
admin.site.register(Projefoto, ProjefotoAdmin)
admin.site.register(Daire, DaireAdmin)