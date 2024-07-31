from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import UsuarioChofer
from .models import Usuario, UsuarioChofer
from . models import Movimientos
from .forms import MovimientosForm
from django.db.models import Sum, Count, F


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
### Lista los campos del Chofer ###
def listmovimiento(request):
    movimientos = Movimientos.objects.all()
    context = {
        'movimientos': movimientos,
    }
    return render(request, 'movimientos/listmovimiento.html', context)

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
