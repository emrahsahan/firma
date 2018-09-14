from django.contrib import admin
from .models import Insaat
'''
from .models import Proje
from .models import Musteri
from .models import Musterigecmisi
from .models import Projefoto
from .models import Blog
from .models import Blogresim
# Register your models here.
'''
class InsaatAdmin(admin.ModelAdmin):

    list_display = ['adi', 'sahibi', 'telefon', 'telefon2', 'email']
    list_display_links = ['adi', 'sahibi', 'telefon', 'telefon2', 'email']
    list_filter = ['adi']
    search_fields = ['adi', 'sahibi']

    class Meta:
       model = Insaat

'''
class ProjeAdmin(admin.ModelAdmin):

    list_display = ['projeadi']
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

class MusteriAdmin(admin.ModelAdmin):

    list_display = ['musteriadi', 'kimlikno', 'telefon', 'email']
    list_filter = ['musteriadi']
    search_fields = ['musteriadi', 'kimlikno']

    class Meta:
        model = Musteri

class MusterigecmisiAdmin(admin.ModelAdmin):

    # bu kod dropdownda alfabetik sıralama yapıyor.
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "musteri":
            kwargs["queryset"] = Musteri.objects.order_by('musteriadi')
        return super(MusterigecmisiAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ['musteri', 'gecmis', 'tarih']
    search_fields = ['musteri__musteriadi']

    class Meta:
        model = Musterigecmisi


class BlogAdmin(admin.ModelAdmin):

    list_display = ['baslik', 'tarih', 'resim', 'aktif']
    list_filter = ['tarih']
    search_fields = ['baslik']

    class Meta:
        model = Blog

class BlogresimAdmin(admin.ModelAdmin):

    list_display = ['blog', 'resimb']
    list_filter = ['blog']
    search_fields = ['blog__baslik']

    class Meta:
        model = Blogresim

'''
admin.site.register(Insaat, InsaatAdmin)

'''
admin.site.register(Proje, ProjeAdmin)
admin.site.register(Musteri, MusteriAdmin)
admin.site.register(Musterigecmisi, MusterigecmisiAdmin)
admin.site.register(Projefoto, ProjefotoAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Blogresim, BlogresimAdmin)

'''