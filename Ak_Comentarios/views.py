from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Comentario
from .forms import ComentarioForms
###########################################################
#Para Comentar
class ComentarioListView(ListView):
    model = Comentario
    template_name = 'Ak_Comentarios/comentar_list.html'
    context_object_name = 'comentarios'

class ComentarioDetailView(DetailView):
    model = Comentario
    template_name = 'Ak_Comentarios/comentar_detail.html'
    
class ComentarioCreateView(CreateView):
    model = Comentario
    template_name = 'Ak_Comentarios/comentar_form.html'
    fields = ['autor', 'asunto', 'contenido', 'nombre_asistente']
    success_url = reverse_lazy('comentar_list')
    
class ComentarioUpdateView(UpdateView):
    model = Comentario
    template_name = 'Ak_Comentarios/comentar_form.html'
    fields = ['asunto', 'contenido']
    success_url = reverse_lazy('comentar_list')
    
class ComentarioDeleteView(DeleteView):
    model = Comentario
    template_name = 'Ak_Comentarios/comentar_delete.html'
    success_url = reverse_lazy('comentar_list')


