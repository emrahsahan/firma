from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
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
