from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify

# Create your models here

class Blog(models.Model):
    baslik = models.CharField(max_length=120, verbose_name='Yazı Başlığı')
    detay = RichTextField(verbose_name='Detay')
    tarih = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')
    resim = models.ImageField(verbose_name='Haber Resmi', null=True)
    aktif = models.BooleanField(default=True, verbose_name='Haber yayınlansın mı?')
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    class Meta:
        verbose_name_plural = 'Haberler'
        ordering = ['-tarih']

    def __str__(self):
        return self.baslik

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug, 'id': self.id})

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.baslik.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Blog, self).save(*args, **kwargs)

class Blogresim(models.Model):
    blog = models.ForeignKey(Blog, related_name='resimler', on_delete=models.CASCADE)
    resimb = models.ImageField(verbose_name='Resim Seç')

    class Meta:
        verbose_name_plural = 'Haber Resimleri'
# Create your models here.