from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify

class Proje(models.Model):
    projeadi = models.CharField(max_length=120, verbose_name='Proje Adı')
    aciklama = RichTextField(verbose_name='Açıklama')
    resim = models.ImageField(verbose_name='Proje Resmi', null=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)
    tarih = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')

    class Meta:
        verbose_name_plural = 'Projeler'
        ordering = ['-tarih']

    def __str__(self):
        return self.projeadi

    def get_absolute_url(self):
        return reverse('proje:detail', kwargs={'slug': self.slug, 'id': self.id})

    def get_create_url(self):
        return reverse('proje:create')

    def get_update_url(self):
        return reverse('proje:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('proje:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.projeadi.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Proje.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Proje, self).save(*args, **kwargs)

class Projefoto(models.Model):
    proje = models.ForeignKey(Proje, related_name='projeresimler', on_delete=models.CASCADE)
    fotograf = models.ImageField(verbose_name='Proje Resmi')

    class Meta:
        verbose_name_plural = 'Proje Fotoğrafları'

class Daire(models.Model):
    proje = models.ForeignKey(Proje, on_delete=models.CASCADE)
    daireno = models.CharField(max_length=120, verbose_name='Daire No')
    kat = models.CharField(max_length=120, verbose_name='Bulunduğu Kat')
    oda = models.CharField(max_length=120, verbose_name='Oda Sayısı')
    alan = models.CharField(max_length=120, verbose_name='Dairenin Alanı')
    blok = models.CharField(max_length=100, verbose_name='Blok Adı')
    isinma = models.CharField(max_length=120, verbose_name='Isınma Tipi')
    yon = models.CharField(max_length=120, verbose_name='Dairenin Yönü')
    satis = models.BooleanField(verbose_name='Satış Durumu')
    aciklama = RichTextField(verbose_name='Açıklama', null=True)

    class Meta:
        verbose_name_plural = 'Dairelerimiz'