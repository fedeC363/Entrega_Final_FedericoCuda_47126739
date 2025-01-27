from django import forms
from .models import Comentario, Comprar, Reservar

class ComentarioForms(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'asunto', 'contenido', 'nombre_asistente']

class ComprarForms(forms.ModelForm):
    class Meta:
        model = Comprar
        fields = ['modelo', 'talle', 'mail', 'direccion', 'banco']

class ReservarForms(forms.ModelForm):
    class Meta:
        model = Reservar
        fields = ['model', 'talle', 'mail', 'fecha']
