from django.contrib import admin
from .models import Temizlik
# Register your models here.

class TemizlikAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'tarih', 'resim']

    class Meta:
        model = Temizlik

admin.site.register(Temizlik, TemizlikAdmin)
