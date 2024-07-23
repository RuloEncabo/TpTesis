from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movimiento

class MovimientoCreateView(CreateView):
    model = Movimiento
    fields = '__all__'  # Puedes especificar los campos explícitamente
    template_name = 'movimiento_form.html'
    success_url = reverse_lazy('movimiento-list')

class MovimientoListView(ListView):
    model = Movimiento
    template_name = 'movimiento_list.html'

class MovimientoUpdateView(UpdateView):
    model = Movimiento
    fields = '__all__'  # Puedes especificar los campos explícitamente
    template_name = 'movimiento_form.html'
    success_url = reverse_lazy('movimiento-list')

class MovimientoDeleteView(DeleteView):
    model = Movimiento
    template_name = 'movimiento_confirm_delete.html'
    success_url = reverse_lazy('movimiento-list')