from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.

class Emlak(models.Model):
    durum_choice = (('1', 'Satılık'), ('2', 'Kiralık'),)
    durum = models.CharField(max_length=1, choices=durum_choice, default=1, verbose_name='Emlak Durumu')
    ilanno = models.CharField(max_length=20, verbose_name='İlan No')
    tip = models.CharField(max_length=50, verbose_name='Emlak Tipi', null=True)
    oda = models.CharField(max_length=50, verbose_name='Oda Sayısı', null=True)
    kat = models.CharField(max_length=50, verbose_name='Bulunduğu Kat', null=True)
    buyukluk = models.CharField(max_length=20, verbose_name='Büyüklük')
    fiyat = models.CharField(max_length=50, verbose_name='Fiyatı')
    resim = models.ImageField(upload_to='emlak/%Y/%m/%d', verbose_name='Fotoğraf')
    aciklama = RichTextField(verbose_name='Açıklama', null=True)
    isinmatipi = models.CharField(max_length=100, verbose_name='Isınma Tipi', null=True)
    il = models.CharField(max_length=30, verbose_name='Bulunduğu İl')
    ilce = models.CharField(max_length=50, verbose_name='Bulunduğu İlçe')
    mahalle = models.CharField(max_length=50, verbose_name='Bulunduğu Mahalle')
    adres = models.TextField(verbose_name='Adres', null=True)
    aktif = models.BooleanField(verbose_name='Aktif İlan', default=True)
    tarih = models.DateTimeField(verbose_name='İlan Tarihi', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Emlak İlanları'
        ordering = ['-tarih']

    def __str__(self):
        return self.ilanno

    def get_absolute_url(self):
        return reverse('emlak:detail', kwargs={'id': self.id})

    def get_create_url(self):
        return reverse('emlak:create')

    def get_update_url(self):
        return reverse('emlak:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('emlak:delete', kwargs={'id': self.id})

class EmlakFoto(models.Model):
    emlak = models.ForeignKey(Emlak, related_name='resimler', on_delete=models.CASCADE)
    resim = models.ImageField(upload_to='emlak/%Y/%m/%d', verbose_name='Resim')

    class Meta:
        verbose_name_plural = 'Emlak Resimleri'


