from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.
class Temizlik(models.Model):
    baslik = models.CharField(max_length=120, verbose_name='Yazı Başlığı')
    detay = RichTextField(verbose_name='Detay')
    tarih = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')
    resim = models.ImageField(verbose_name='Temizlik Resmi', null=True)

    class Meta:
        verbose_name_plural = 'Temizlik Hizmetleri'

    def __str__(self):
        return self.baslik