from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Comprar
from .forms import ComprarForms
###########################################################
#Para comprar
class ComprarListView(ListView):
    model = Comprar
    template_name = 'Ak_comprar/comprar_list.html'
    context_object_name = 'comprar'

class ComprarDetailView(DetailView):
    model = Comprar
    template_name = 'Ak_comprar/comprar_detail.html'
    
class ComprarCreateView(CreateView):
    model = Comprar
    template_name = 'Ak_comprar/comprar_form.html'
    fields = ['modelo', 'talle', 'mail', 'direccion', 'banco']
    success_url = reverse_lazy('comprar_list')
    
class ComprarUpdateView(UpdateView):
    model = Comprar
    template_name = 'Ak_comprar/comprar_form.html'
    fields = ['modelo', 'talle', 'direccion']
    success_url = reverse_lazy('comprar_list')
    
class ComprarDeleteView(DeleteView):
    model = Comprar
    template_name = 'Ak_comprar/comprar_delete.html'
    success_url = reverse_lazy('comprar_list')



    
    
    
    
    
    
    
    
    
    
    
    
    
    
