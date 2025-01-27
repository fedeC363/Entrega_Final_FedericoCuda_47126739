from django import forms
from .models import Comentario

class ComentarioForms(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'asunto', 'contenido', 'nombre_asistente']

