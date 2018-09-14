from django.db import models

# Create your models here.

class Foto(models.Model):
    aciklama = models.CharField(max_length=200, verbose_name='Açıklama')
    image = models.ImageField(upload_to='uploads/', verbose_name='Resim')

    class Meta:
        verbose_name_plural = 'Resimler'

    def __str__(self):
        return self.aciklama