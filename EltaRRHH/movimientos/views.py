from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import UsuarioChofer
from django.db.models import Sum, Count, F
#import pandas as pd
from .models import Movimientos
from chofer.models import Chofer
from .forms import MovimientosForm

@login_required
def registrarmovimiento(request):
    if request.method == 'POST':
        form = MovimientosForm(request.POST)
        if form.is_valid():
            try:
                usuario = request.user

                # Verificar si el usuario es un chofer
                try:
                    chofer = Chofer.objects.get(usuario=usuario)
                except Chofer.DoesNotExist:
                    chofer = None

                # Crear el movimiento
                Movimientos.objects.create(
                    usuario_id=usuario,  # Usuario actual
                    chofer=chofer,  # Puede ser None si el usuario no es un chofer
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
                
                messages.success(request, 'Movimiento registrado exitosamente.')
                return redirect('listmovimiento')
            except Exception as e:
                messages.error(request, f'Error inesperado: {str(e)}')
        else:
            messages.error(request, 'Formulario inválido. Por favor, revisa los datos ingresados.')
    else:
        form = MovimientosForm()

    return render(request, 'movimientos/registrarmovimiento.html', {'form': form})


### Lista los campos del Chofer ###
def listmovimiento(request):
    movimientos = Movimientos.objects.all()
    context = {
        'movimientos': movimientos,
    }
    return render(request, 'movimientos/listmovimiento.html', context)


### Lista los campos del Chofer que esta logeado ###
@login_required
@login_required
def listmovimientoChofer(request):
    usuario = request.user
    try:
        # Obtener el chofer asociado al usuario registrado
        chofer = Chofer.objects.get(usuario=usuario)
        # Filtrar movimientos del chofer
        movimientos = Movimientos.objects.filter(chofer=chofer)
    except Chofer.DoesNotExist:
        # Si no existe el chofer, no hay movimientos para mostrar
        movimientos = Movimientos.objects.none()

    # Calcular la diferencia entre kmInicio y kmFin para cada movimiento
    for movimiento in movimientos:
        movimiento.km_difference = (movimiento.kmFin or 0) - movimiento.kmInicio

    context = {
        'movimientos': movimientos,
    }
    return render(request, 'movimientos/list_mov_chofer.html', context)



def movimiento(request):
    # Total de kilómetros realizados
    total_km = Movimientos.objects.aggregate(total_km=Sum(F('kmFin') - F('kmInicio')))['total_km']
    
    # Total de movimientos
    total_movimientos = Movimientos.objects.count()

    
    # Total de choferes que realizaron registros
    total_choferes = Movimientos.objects.values('chofer').distinct().count()
    
    # Total de registros realizados por chofer
    registros_por_chofer = Movimientos.objects.values('chofer').annotate(total_registros=Count('mov_id')).order_by('-total_registros')
    
    context = {
        'total_km': total_km,
        'total_choferes': total_choferes,
        'registros_por_chofer': registros_por_chofer,
        'total_movimientos': total_movimientos,
    }
    return render(request, 'movimientos/movimiento.html', context)

### Lista los campos del Chofer ###
def listusuariochofer(request):
    usuarioschofer = UsuarioChofer.objects.all()
    context = {
        'usuarioschofer': usuarioschofer,
    }
    return render(request, 'chofer/listusuariochofer.html', context)
    
