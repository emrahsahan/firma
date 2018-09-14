from django.contrib import admin
from .models import Blog
from .models import Blogresim


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'tarih', 'resim', 'aktif', 'slug']
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


admin.site.register(Blog, BlogAdmin)
admin.site.register(Blogresim, BlogresimAdmin)

