from django import forms
from .models import Emlak

class EmlakForm(forms.ModelForm):

    class Meta:
        model = Emlak
        fields = [
            'durum',
            'ilanno',
            'resim',
            'aktif',
            'tip',
            'oda',
            'kat',
            'buyukluk',
            'fiyat',
            'resim',
            'aciklama',
            'isinmatipi',
            'il',
            'ilce',
            'mahalle',
            'adres',
            'aktif',
        ]