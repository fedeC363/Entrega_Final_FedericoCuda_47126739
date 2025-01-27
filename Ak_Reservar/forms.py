from .models import Reservar
from django import forms

class ReservarForms(forms.ModelForm):
    class Meta:
        model = Reservar
        fields = ['modelo', 'talle', 'mail', 'fecha']