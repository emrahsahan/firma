from django.contrib import admin
from .models import Musteri
from .models import Musterigecmisi
# Register your models here.

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

admin.site.register(Musteri, MusteriAdmin)
admin.site.register(Musterigecmisi, MusterigecmisiAdmin)
