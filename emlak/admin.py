from django.contrib import admin
from .models import Emlak
from .models import EmlakFoto
# Register your models here.

class EmlakAdmin(admin.ModelAdmin):
    list_display = ['durum','ilanno', 'tip', 'oda', 'fiyat', 'aktif', 'buyukluk', 'ilce', 'mahalle']
    list_filter = ['tarih', 'durum']
    search_fields = ['ilanno', 'fiyat', 'durum', 'ilce', 'mahalle']
    list_display_links = ['durum', 'tip', 'oda', 'fiyat', 'aktif', 'buyukluk', 'ilce', 'mahalle']


    class Meta:
        model = Emlak


class EmlakFotoAdmin(admin.ModelAdmin):
    list_display = ['emlak', 'resim']
    list_filter = ['emlak']
    search_fields = ['emlak__ilanno']

    class Meta:
        model = EmlakFoto

admin.site.register(Emlak, EmlakAdmin)
admin.site.register(EmlakFoto, EmlakFotoAdmin)