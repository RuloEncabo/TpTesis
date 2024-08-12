import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from django.db.models import Sum, Count, F
#import pandas as pd
from .models import Movimientos
from chofer.models import Chofer
from .forms import MovimientosForm
from django.db.models.functions import TruncMonth

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


### Solo registra elChofer ###
@login_required
def registrarmovimientoc(request):
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
                return redirect('movimientoc')
            except Exception as e:
                messages.error(request, f'Error inesperado: {str(e)}')
        else:
            messages.error(request, 'Formulario inválido. Por favor, revisa los datos ingresados.')
    else:
        form = MovimientosForm()

    return render(request, 'movimientos/registrarmovimientoc.html', {'form': form})

### Lista los campos del Chofer ###
def listmovimiento(request):
    movimientos = Movimientos.objects.all()
    # Calcular la diferencia entre kmInicio y kmFin para cada movimiento
    for movimiento in movimientos:
        movimiento.km_difference = (movimiento.kmFin or 0) - movimiento.kmInicio
    context = {
        'movimientos': movimientos,
    }
    return render(request, 'movimientos/listmovimiento.html', context)

### Lista los campos del Chofer que esta logeado ###
@login_required
def listmovimientoChofer(request):
    usuario = request.user
    try:
        chofer = Chofer.objects.get(usuario=usuario)
        movimientos = Movimientos.objects.filter(chofer=chofer)
    except Chofer.DoesNotExist:
        movimientos = Movimientos.objects.none()
        # O podrías redirigir a una página de error si prefieres

    # Calcular la diferencia entre kmInicio y kmFin para cada movimiento
    for movimiento in movimientos:
        movimiento.km_difference = (movimiento.kmFin or 0) - movimiento.kmInicio

    context = {
        'movimientos': movimientos,
    }
    return render(request, 'movimientos/list_mov_chofer.html', context)

### Muestra Resumen Choferes en sesion ###
def movchofer(request):
    # Obtener el chofer asociado al usuario autenticado
    chofer = request.user.chofer

    # Total de kilómetros realizados por el chofer
    total_km = Movimientos.objects.filter(chofer=chofer).aggregate(total_km=Sum(F('kmFin') - F('kmInicio')))['total_km']
    
    # Total de movimientos realizados por el chofer
    total_movimientos = Movimientos.objects.filter(chofer=chofer).count()

    # Total de registros realizados por el chofer
    registros_por_chofer = Movimientos.objects.filter(chofer=chofer).values('chofer').annotate(total_registros=Count('mov_id')).order_by('-total_registros')
    
    context = {
        'total_km': total_km,
        'total_choferes': 1,  # Solo se considera el chofer logueado
        'registros_por_chofer': registros_por_chofer,
        'total_movimientos': total_movimientos,
    }
    return render(request, 'movimientos/movchofer.html', context)


### Muestra Resumen de todos los Choferes ###
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

### Funcion para determinar moviento por Chofer ###
def movimientoc(request):
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
    usuarioschofer = Chofer.objects.all()
    context = {
        'usuarioschofer': usuarioschofer,
    }
    return render(request, 'chofer/listusuariochofer.html', context)


## Funciones para Graficos ###
@login_required
def kpi(request):
    # Obtener el mes actual y el mes anterior
    fecha_actual = datetime.date.today()
    mes_actual = fecha_actual.month
    anio_actual = fecha_actual.year
    
    # Obtener los datos de tipos de kilómetros registrados en el último mes
    datos_km_tipos = Movimientos.objects.filter(
        fin__year=anio_actual,
        fin__month=mes_actual
    ).values('tipo_kilometro__descripcion').annotate(
        total_km=Sum('kmFin') - Sum('kmInicio')
    ).order_by('tipo_kilometro__descripcion')

    labels_km_tipos = [dato['tipo_kilometro__descripcion'] for dato in datos_km_tipos]
    series_km_tipos = [dato['total_km'] for dato in datos_km_tipos]

    # Obtener los datos de kilómetros por mes
    datos_por_mes = Movimientos.objects.annotate(
        mes=TruncMonth('fin')
    ).values('mes').annotate(
        total_km=Sum('kmFin') - Sum('kmInicio')
    ).order_by('mes')

    # Filtrar los datos que no tienen 'mes' como None
    datos_por_mes = [dato for dato in datos_por_mes if dato['mes'] is not None]

    labels_meses = [dato['mes'].strftime('%Y-%m') for dato in datos_por_mes]
    series_meses = [dato['total_km'] for dato in datos_por_mes]

    # Obtener los datos de kilómetros por chofer
    choferes = Chofer.objects.all()
    labels_choferes = []
    series_choferes = []

    for chofer in choferes:
        labels_choferes.append(chofer.nombre)
        km_total = Movimientos.objects.filter(chofer=chofer).aggregate(
            total_km=Sum('kmFin') - Sum('kmInicio')
        )['total_km']
        series_choferes.append(km_total or 0)  # Si no hay movimientos, km_total será None
        
    # Contar usuarios por rol
    usuarios_por_tipo = Usuario.objects.values('role').annotate(count=Count('id'))
    # Asumiendo que tienes dos roles, 'Chofer' y 'Usuario'
    roles = ['Chofer', 'User']  # Ajusta estos nombres a los roles reales que tienes
    # Inicializar los conteos en 0
    conteos = {rol: 0 for rol in roles}
    # Contar usuarios por rol
    for item in usuarios_por_tipo:
        rol = item['role']
        conteos[rol] = item['count']
    # Preparar los datos para el gráfico
    labels_tipo = list(conteos.keys())
    series_tipo = list(conteos.values())
    
    context = {
        'labels_choferes': labels_choferes,
        'series_choferes': series_choferes,
        'labels_meses': labels_meses,
        'series_meses': series_meses,
        'labels_tipo': labels_tipo,
        'series_tipo': series_tipo,
        'labels_km_tipos':labels_km_tipos,
        'series_km_tipos':series_km_tipos
    }
    return render(request, 'movimientos/analitica.html', context)
    
