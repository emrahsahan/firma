from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Insaat(models.Model):
    adi = models.CharField(max_length=120, verbose_name='Firma Adı', null=False, blank=False)
    sahibi = models.CharField(max_length=120, verbose_name='Firma Sahibi', null=False, blank=False)
    telefon = models.CharField(max_length=11, verbose_name='İş Telefonu', null=True)
    telefon2 = models.CharField(max_length=11, verbose_name='Cep Telefonu', null=True)
    faks = models.CharField(max_length=11, verbose_name='Faks Numarası', null=True)
    email = models.EmailField(verbose_name='Email Adresi', null=True)
    adres = models.TextField(verbose_name='Adres', null=True)
    hakkimizda = RichTextField(verbose_name='Hakkımızda', null=True)
    vizyon = RichTextField(verbose_name='Vizyonumuz', null=True)
    misyon = RichTextField(verbose_name='Misyonumuz', null=True)
    facebook = models.CharField(max_length=120, verbose_name='Facebook', null=True)
    twitter = models.CharField(max_length=120, verbose_name='Twitter', null=True)
    youtube = models.CharField(max_length=120, verbose_name='Youtube', null=True)
    instagram = models.CharField(max_length=120, verbose_name='Instagram', null=True)
    googlemap = models.TextField(verbose_name='Google Map', null=True)

    class Meta:
        verbose_name_plural = 'Firmalar'

    def __str__(self):
        return self.adi
'''
class Proje(models.Model):
    projeadi = models.CharField(max_length=120, verbose_name='Proje Adı')
    aciklama = RichTextField(verbose_name='Açıklama')
    resim = models.ImageField(verbose_name='Proje Resmi', null=True)

    class Meta:
        verbose_name_plural = 'Projeler'

    def __str__(self):
        return self.projeadi

class Projefoto(models.Model):
    proje = models.ForeignKey(Proje, on_delete=models.CASCADE)
    fotograf = models.ImageField(verbose_name='Proje Resmi')

    class Meta:
        verbose_name_plural = 'Proje Fotoğrafları'

class Musteri(models.Model):
    musteriadi = models.CharField(max_length=120, verbose_name='Müşteri Adı')
    kimlikno = models.CharField(max_length=11, null=True, verbose_name='T.C Kimlik No')
    telefon = models.CharField(max_length=11, verbose_name='Telefon')
    email = models.EmailField(verbose_name='E-mail Adresi', null=True)
    adres = models.TextField(verbose_name='Adres', null=True)
    dogumtarihi = models.DateField(verbose_name='Doğum Tarihi', null=True)

    class Meta:
        verbose_name_plural = 'Müşteriler'

    def __str__(self):
        return self.musteriadi

class Musterigecmisi(models.Model):
    musteri = models.ForeignKey(Musteri, on_delete=models.CASCADE)
    gecmis = models.TextField(max_length=250, verbose_name='Müşteri Bilgisi')
    tarih = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')

    class Meta:
        verbose_name_plural = 'Müşteri Geçmişleri'


    def __str__(self):
        return self.gecmis

class Blog(models.Model):
    baslik = models.CharField(max_length=120, verbose_name='Yazı Başlığı')
    detay = RichTextField(verbose_name='Detay')
    tarih = models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')
    resim = models.ImageField(verbose_name='Haber Resmi', null=True)
    aktif = models.BooleanField(default=True, verbose_name='Haber yayınlansın mı?')

    class Meta:
        verbose_name_plural = 'Haberler'


    def __str__(self):
        return self.baslik

class Blogresim(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    resimb = models.ImageField(verbose_name='Resim Seç')

    class Meta:
        verbose_name_plural = 'Haber Resimleri'

'''