from pyexpat.errors import messages
from django.forms import ValidationError
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import UsuarioChofer
from .models import Usuario, UsuarioChofer
from . models import Movimientos
from django.urls import reverse_lazy
from .forms import MovimientosForm


@login_required
def registrarmovimiento(request):
    if request.method == 'POST':
        form = MovimientosForm(request.POST)
        if form.is_valid():
            usuario = request.user  # Asegúrate de usar `request.user`
            chofer = None

            if usuario.role == 'chofer':
                try:
                    usuario_chofer = UsuarioChofer.objects.get(usuario=usuario)
                    chofer = usuario_chofer
                except UsuarioChofer.DoesNotExist:
                    form.add_error(None, "El usuario no es un chofer registrado.")
                    return render(request, 'movimientos/registrarmovimiento.html', {'form': form})

            Movimientos.objects.create(
                usuario=usuario,
                chofer=chofer,
                nFlota=form.cleaned_data['nFlota'],
                inicio=form.cleaned_data['inicio'],
                fin=form.cleaned_data['fin'],
                kmInicio=form.cleaned_data['kmInicio'],
                kmFin=form.cleaned_data['kmFin'],
                lugar_inicio=form.cleaned_data['lugar_inicio'],
                lugar_fin=form.cleaned_data['lugar_fin'],
                tipo_kilometro=form.cleaned_data['tipo_kilometro'],
                lleva_carga=form.cleaned_data['lleva_carga'],
                permanencia=form.cleaned_data['permanencia'],
                diasPermanencia=form.cleaned_data['diasPermanencia'],
                cruce_frontera=form.cleaned_data['cruce_frontera'],
                comentarios=form.cleaned_data['comentarios'],
            )
            return redirect('movimiento_lista')
    else:
        form = MovimientosForm()
    
    return render(request, 'movimientos/registrarmovimiento.html', {'form': form})

"""@login_required
def registrarmovimiento(request):
    if request.method == 'POST':
        form = MovimientosForm(request.POST)
        if form.is_valid():
            usuario = request.user
            if usuario.role == 'chofer':
                try:
                    usuario_chofer = UsuarioChofer.objects.get(usuario=usuario)
                    Movimientos.objects.create(
                        usuario=usuario,
                        usuario_chofer=usuario_chofer,
                        nFlota=form.cleaned_data['nFlota'],
                        inicio=form.cleaned_data['inicio'],
                        fin=form.cleaned_data['fin'],
                        kmInicio=form.cleaned_data['kmInicio'],
                        kmFin=form.cleaned_data['kmFin'],
                        lugar_inicio=form.cleaned_data['lugar_inicio'],
                        lugar_fin=form.cleaned_data['lugar_fin'],
                        lleva_carga=form.cleaned_data['lleva_carga'],
                        permanencia=form.cleaned_data['permanencia'],
                        diasPermanencia=form.cleaned_data['diasPermanencia'],
                        cruce_frontera=form.cleaned_data['cruce_frontera'],
                        comentarios=form.cleaned_data['comentarios'],
                    )
                    return redirect('movimiento_lista')
                except UsuarioChofer.DoesNotExist:
                    form.add_error(None, "El usuario no es un chofer registrado.")
            else:
                form.add_error(None, "El usuario no tiene el rol de chofer.")
    else:
        form = MovimientosForm()
    
    return render(request, 'movimientos/registrarmovimiento.html', {'form': form})
"""


class MovimientoCreateView(CreateView):
    model = Movimientos
    fields = '__all__'  # Puedes especificar los campos explícitamente
    template_name = 'movimiento_form.html'
    success_url = reverse_lazy('movimiento-list')

class MovimientoListView(ListView):
    model = Movimientos
    template_name = 'movimiento_list.html'

class MovimientoUpdateView(UpdateView):
    model = Movimientos
    fields = '__all__'  # Puedes especificar los campos explícitamente
    template_name = 'movimiento_form.html'
    success_url = reverse_lazy('movimiento-list')

class MovimientoDeleteView(DeleteView):
    model = Movimientos
    template_name = 'movimiento_confirm_delete.html'
    success_url = reverse_lazy('movimiento-list')
    
    
"""
@login_required
def registrar_movimientoViaje(request):
    if request.method == 'POST':
        form = MovimientoForm(request.POST)
        if form.is_valid():
            usuario = request.user
            if usuario.role == 'chofer':
                try:
                    usuario_chofer = UsuarioChofer.objects.get(usuario=usuario)
                    viaje_activo = Viaje.objects.filter(chofer=usuario_chofer, activo=True).first()
                    if not viaje_activo:
                        form.add_error(None, "No hay un viaje activo para registrar el movimiento.")
                    else:
                        tipo_kilometro = form.cleaned_data['tipo_kilometro']
                        movimiento = Movimiento(
                            chofer=usuario_chofer,
                            viaje=viaje_activo,
                            nFlota=form.cleaned_data['nFlota'],
                            inicio=form.cleaned_data['inicio'],
                            fin=form.cleaned_data['fin'],
                            kmInicio=form.cleaned_data['kmInicio'],
                            kmFin=form.cleaned_data['kmFin'],
                            lugar_inicio=form.cleaned_data['lugar_inicio'],
                            lugar_fin=form.cleaned_data['lugar_fin'],
                            tipo_kilometro=tipo_kilometro,
                            lleva_carga=form.cleaned_data['lleva_carga'],
                            permanencia=form.cleaned_data['permanencia'],
                            diasPermanencia=form.cleaned_data['diasPermanencia'],
                            cruce_frontera=form.cleaned_data['cruce_frontera'],
                            comentarios=form.cleaned_data['comentarios'],
                        )
                        movimiento.clean()  # Llama al método clean para validar el movimiento
                        movimiento.save()
                        return redirect('movimiento_lista')
                except UsuarioChofer.DoesNotExist:
                    form.add_error(None, "El usuario no es un chofer registrado.")
                except ValidationError as e:
                    form.add_error(None, e.message)
            else:
                form.add_error(None, "El usuario no tiene el rol de chofer.")
    else:
        form = MovimientoForm()
    
    return render(request, 'movimientos/registrar_movimiento.html', {'form': form})
"""
