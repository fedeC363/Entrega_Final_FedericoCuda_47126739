from django import forms
from .models import Comprar

class ComprarForms(forms.ModelForm):
    class Meta:
        model = Comprar
        fields = ['modelo', 'talle', 'mail', 'direccion', 'banco']

