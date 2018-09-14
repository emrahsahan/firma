from django import forms
from .models import Proje

class ProjeForm(forms.ModelForm):

    class Meta:
        model = Proje
        fields = [
            'projeadi',
            'aciklama',
            'resim',
        ]