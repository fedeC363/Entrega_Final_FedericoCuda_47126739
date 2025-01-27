from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Reservar
from .forms import ReservarForms
###########################################################
#Para Reservar
class ReservaListView(ListView):
    model = Reservar
    template_name = 'Ak_Reservar/reservar_list.html'
    context_object_name = 'reservas'

class ReservaDetailView(DetailView):
    model = Reservar
    template_name = 'Ak_Reservar/reservar_detail.html'
    
class ReservaCreateView(CreateView):
    model = Reservar
    template_name = 'Ak_Reservar/reservar_form.html'
    fields = ['modelo', 'talle', 'mail', 'fecha']
    success_url = reverse_lazy('reservar_list')
    
class ReservaUpdateView(UpdateView):
    model = Reservar
    template_name = 'Ak_Reservar/reservar_form.html'
    fields = ['modelo', 'talle', 'fecha']
    success_url = reverse_lazy('reservar_list')
    
class ReservaDeleteView(DeleteView):
    model = Reservar
    template_name = 'Ak_Reservar/reservar_delete.html'
    success_url = reverse_lazy('reservar_list')
