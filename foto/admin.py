from django.contrib import admin
from .models import Foto
# Register your models here.

class FotoAdmin(admin.ModelAdmin):
    list_display = ['image', 'aciklama']

    class Meta:
        model = Foto

admin.site.register(Foto, FotoAdmin)