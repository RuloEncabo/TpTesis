import datetime
import calendar
from datetime import datetime
from datetime import timedelta, timezone
from datetime import datetime
from datetime import date
from django.db.models.functions import Coalesce, Greatest
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from django.db.models import Sum,Count,F,Value,ExpressionWrapper, IntegerField, Q
from .models import Movimientos
from chofer.models import Chofer 
from .forms import MovimientosForm, MovFinForm,MovInicioForm
from django.db.models.functions import TruncMonth
from django.utils.timezone import now


@login_required
def registrarmovimiento(request):
    if request.method == 'POST':
        form = MovimientosForm(request.POST)
        if form.is_valid():
            try:
                usuario = request.user

                # Verifica si el usuario es un chofer
                try:
                    chofer = Chofer.objects.get(usuario=usuario)
                except Chofer.DoesNotExist:
                    chofer = None

                # Crea el movimiento
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
###########################################################################
############################## Solo registra el Chofer ##############################
@login_required
def registrarmovimientoc(request):
    if request.method == 'POST':
        form = MovimientosForm(request.POST)
        if form.is_valid():
            try:
                usuario = request.user

                # Verifica si el usuario es un chofer
                try:
                    chofer = Chofer.objects.get(usuario=usuario)
                except Chofer.DoesNotExist:
                    chofer = None

                # Crea el movimiento
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

    return render(request, 'movimientos/registrarmovimientoc.html', {'form': form})

###########################################################################
##########################       Chofer      ##############################
###########################################################################

############################## Inicio Movimiento ##############################
@login_required
def inicioMov(request):
    if request.method == 'POST':
        form = MovInicioForm(request.POST)
        if form.is_valid():
            try:
                usuario = request.user
                # Verifica si el usuario es un chofer
                try:
                    chofer = Chofer.objects.get(usuario=usuario)
                except Chofer.DoesNotExist:
                    chofer = None

                # Crea el movimiento 
                Movimientos.objects.create(
                    usuario_id=usuario,  # Usuario actual
                    chofer=chofer,  # Puede ser None si el usuario no es un chofer
                    nFlota=form.cleaned_data['nFlota'],
                    inicio=form.cleaned_data['inicio'],
                    kmInicio=form.cleaned_data['kmInicio'],
                    tipo_kilometro=form.cleaned_data['tipo_kilometro'],
                    lugar_inicio=form.cleaned_data['lugar_inicio'],
                    lleva_carga=form.cleaned_data['lleva_carga'],
                )
                
                messages.success(request, 'Movimiento registrado exitosamente.')
                return redirect('movchofer')
            except Exception as e:
                messages.error(request, f'Error inesperado: {str(e)}')
        else:
            messages.error(request, 'Formulario inválido. Por favor, revisa los datos ingresados.')
    else:
        form = MovInicioForm()

    return render(request, 'movimientos/registrarInicio.html', {'form': form})

############################## FIN Movimiento ##############################
def finMov(request, mov_id):
    movimiento = get_object_or_404(Movimientos, mov_id=mov_id)

    if request.method == 'POST':
        form = MovFinForm(request.POST)
        if form.is_valid():
            kmFin = form.cleaned_data['kmFin']
            
            # comprueba que kmFin sea mayor que kmInicio
            if kmFin <= movimiento.kmInicio:
                messages.error(request, 'El kilometraje final debe ser mayor que el kilometraje inicial.')
            else:
                try:
                    # Actualiza los campos relacionados con el fin del movimiento
                    movimiento.fin = form.cleaned_data['fin']
                    movimiento.kmFin = kmFin
                    movimiento.lugar_fin = form.cleaned_data['lugar_fin']
                    movimiento.permanencia = form.cleaned_data['permanencia']
                    movimiento.diasPermanencia = form.cleaned_data['diasPermanencia']
                    movimiento.cruce_frontera = form.cleaned_data['cruce_frontera']
                    movimiento.comentarios = form.cleaned_data['comentarios']

                    # Guarda los cambios
                    movimiento.save()
                    
                    messages.success(request, 'Fin del movimiento registrado exitosamente.')
                    return redirect('movchofer')
                except Exception as e:
                    messages.error(request, f'Error al registrar el fin del movimiento: {str(e)}')
        else:
            print(form.errors)  # Ver los errores del formulario en la consola
            messages.error(request, 'Formulario inválido. Por favor, revisa los datos ingresados.')
    else:
        form = MovFinForm(initial={'movimiento_id': movimiento.mov_id})

    return render(request, 'movimientos/registrarFin.html', {'form': form, 'movimiento': movimiento})

############################## Modificar Movimiento Chofer  mes en Curso ##############################
def modificarmovimiento(request, mov_id):
    movimiento = get_object_or_404(Movimientos, pk=mov_id)  
    # fecha de fin del movimiento
    fecha_fin = movimiento.fin
    # Verifica si la fecha de fin está definida
    if fecha_fin is not None:
        # obtine el mes y el año actuales
        mes_actual = datetime.now().month
        año_actual = datetime.now().year

        # Verifica si el movimiento pertenece al mes y año actuales
        if fecha_fin.month == mes_actual and fecha_fin.year == año_actual:
            form = MovimientosForm(instance=movimiento)

            if request.method == 'POST':
                form = MovimientosForm(request.POST, instance=movimiento)
                if form.is_valid():
                    form.save()
                    return redirect('movchofer')
            
            context = {
                'form': form,
                'movimiento': movimiento,
            }
            return render(request, 'movimientos/modificarmovimiento.html', context)
        else:
            # aviso al usuario
            messages.error(request, "Este movimiento no puede ser modificado porque no pertenece al mes en curso. Por favor, comuníquese con RRHH.")
            return redirect('movchofer')  
    else:
        # aviso al usuario sobre la falta de fecha
        messages.error(request, "No se puede modificar el movimiento porque no tiene una fecha de fin válida. Por favor, Cierre el Movimiento.")
        return redirect('movchofer')  
    
############################## Borrar Movimiento Chofer ##############################
@login_required
def borrarmovimiento(request):
    if request.method == 'POST':
        movimiento_id = request.POST.get('id')
        try:
            movimiento = get_object_or_404(Movimientos, mov_id=movimiento_id)
            movimiento.delete()
            return JsonResponse({'success': True})
        except Movimientos.DoesNotExist:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})

###########################################################################
##########################        RRHH       ##############################
###########################################################################

############################## Modificar Movimiento ##############################
@login_required
def modimovR(request, mov_id):
    # se obtiene el movimiento por su ID o devuelve un 404 si no existe
    movimiento = get_object_or_404(Movimientos, pk=mov_id)
    
    # Obtiene la fecha de fin del movimiento
    fecha_fin = movimiento.fin
    
    # Verifica si la fecha de fin está definida
    if fecha_fin is not None:
        # Instancia el formulario con el movimiento actual
        form = MovimientosForm(instance=movimiento)

        if request.method == 'POST':
            form = MovimientosForm(request.POST, instance=movimiento)
            if form.is_valid():
                form.save()
                messages.success(request, "El movimiento se ha modificado correctamente.")
                return redirect('listmovimiento')
        context = {
            'form': form,
            'movimiento': movimiento,
        }
        return render(request, 'movimientos/modimovR.html', context)
    else:
        # Informa al usuario que el movimiento no tiene una fecha de fin válida
        messages.error(request, "No se puede modificar el movimiento porque no tiene una fecha de fin válida. Por favor, cierre el movimiento.")
        return redirect('listmovimiento')

############################## borrar Movimiento ##############################
@login_required
def borrarmovimientoR(request):
    if request.method == 'POST':
        movimiento_id = request.POST.get('id')
        try:
            movimiento = get_object_or_404(Movimientos, mov_id=movimiento_id)
            movimiento.delete()
            return JsonResponse({'success': True})
        except Movimientos.DoesNotExist:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})

###########################################################################
########################## Inicio Movimiento ##############################

@login_required
def inicioMov(request):
    if request.method == 'POST':
        form = MovInicioForm(request.POST)
        if form.is_valid():
            try:
                usuario = request.user
                # Verificar si el usuario es un chofer
                try:
                    chofer = Chofer.objects.get(usuario=usuario)
                except Chofer.DoesNotExist:
                    chofer = None

                # Crea el movimiento con los campos requeridos
                Movimientos.objects.create(
                    usuario_id=usuario,  # Usuario actual
                    chofer=chofer,  # Puede ser None si el usuario no es un chofer
                    nFlota=form.cleaned_data['nFlota'],
                    inicio=form.cleaned_data['inicio'],
                    kmInicio=form.cleaned_data['kmInicio'],
                    tipo_kilometro=form.cleaned_data['tipo_kilometro'],
                    lugar_inicio=form.cleaned_data['lugar_inicio'],
                    lleva_carga=form.cleaned_data['lleva_carga'],
                )
                
                messages.success(request, 'Movimiento registrado exitosamente.')
                return redirect('movchofer')
            except Exception as e:
                messages.error(request, f'Error inesperado: {str(e)}')
        else:
            messages.error(request, 'Formulario inválido. Por favor, revisa los datos ingresados.')
    else:
        form = MovInicioForm()

    return render(request, 'movimientos/registrarInicio.html', {'form': form})

############################## Registro Fin Movimiento ##############################
def finMov(request, mov_id):
    movimiento = get_object_or_404(Movimientos, mov_id=mov_id)

    if request.method == 'POST':
        form = MovFinForm(request.POST)
        if form.is_valid():
            kmFin = form.cleaned_data['kmFin']
            
            # Verifica que kmFin sea mayor que kmInicio
            if kmFin <= movimiento.kmInicio:
                messages.error(request, 'El kilometraje final debe ser mayor que el kilometraje inicial.')
            else:
                try:
                    # Actualiza los campos relacionados con el fin del movimiento
                    movimiento.fin = form.cleaned_data['fin']
                    movimiento.kmFin = kmFin
                    movimiento.lugar_fin = form.cleaned_data['lugar_fin']
                    movimiento.permanencia = form.cleaned_data['permanencia']
                    movimiento.diasPermanencia = form.cleaned_data['diasPermanencia']
                    movimiento.cruce_frontera = form.cleaned_data['cruce_frontera']
                    movimiento.comentarios = form.cleaned_data['comentarios']

                    # Guarda los cambios
                    movimiento.save()
                    
                    messages.success(request, 'Fin del movimiento registrado exitosamente.')
                    return redirect('movchofer')
                except Exception as e:
                    messages.error(request, f'Error al registrar el fin del movimiento: {str(e)}')
        else:
            print(form.errors)  # Ver los errores del formulario en la consola
            messages.error(request, 'Formulario inválido. Por favor, revisa los datos ingresados.')
    else:
        form = MovFinForm(initial={'movimiento_id': movimiento.mov_id})

    return render(request, 'movimientos/registrarFin.html', {'form': form, 'movimiento': movimiento})


####### Modificar Movimiento Chofer  mes en Curso #######
def modificarmovimiento(request, mov_id):
    movimiento = get_object_or_404(Movimientos, pk=mov_id)  
    # se obtiene la fecha de fin del movimiento
    fecha_fin = movimiento.fin
    # Verifica si la fecha de fin está definida
    if fecha_fin is not None:
        # se obtiene el mes y el año actuales
        mes_actual = datetime.now().month
        año_actual = datetime.now().year

        # Verifica si el movimiento pertenece al mes y año actuales
        if fecha_fin.month == mes_actual and fecha_fin.year == año_actual:
            form = MovimientosForm(instance=movimiento)

            if request.method == 'POST':
                form = MovimientosForm(request.POST, instance=movimiento)
                if form.is_valid():
                    form.save()
                    return redirect('movchofer')
            
            context = {
                'form': form,
                'movimiento': movimiento,
            }
            return render(request, 'movimientos/modificarmovimiento.html', context)
        else:
            # envia mensaje informando al usuario
            messages.error(request, "Este movimiento no puede ser modificado porque no pertenece al mes en curso. Por favor, comuníquese con RRHH.")
            return redirect('movchofer')  
    else:
        # envia mensaje informando al usuario sobre la falta de fecha
        messages.error(request, "No se puede modificar el movimiento porque no tiene una fecha de fin válida. Por favor, Cierre el Movimiento.")
        return redirect('movchofer')  
    
####### Borrar Movimiento Chofer #######
@login_required
def borrarmovimiento(request):
    if request.method == 'POST':
        movimiento_id = request.POST.get('id')
        try:
            movimiento = get_object_or_404(Movimientos, mov_id=movimiento_id)
            movimiento.delete()
            return JsonResponse({'success': True})
        except Movimientos.DoesNotExist:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})

###########################################################################
############################ Listas y Reportes ############################
###########################################################################

####### Lista los campos del Chofer #######
def listmovimiento(request):
    # Obtien todos los movimientos y calcula la diferencia entre kmInicio y kmFin, mostrando 0 si es negativa
    movimientos = Movimientos.objects.annotate(
        km_difference=Greatest(Coalesce(F('kmFin'), Value(0)) - F('kmInicio'), Value(0))
    )
    
    context = {
        'movimientos': movimientos,
    }
    return render(request, 'movimientos/listmovimiento.html', context)

####### Lista los campos del Chofer que esta logeado #######
@login_required
def listmovimientoChofer(request):
    usuario = request.user
    try:
        chofer = Chofer.objects.get(usuario=usuario)
        movimientos = Movimientos.objects.filter(chofer=chofer)
    except Chofer.DoesNotExist:
        movimientos = Movimientos.objects.none()
       

    # Calcula la diferencia entre kmInicio y kmFin para cada movimiento
    for movimiento in movimientos:
        movimiento.km_difference = (movimiento.kmFin or 0) - movimiento.kmInicio

    context = {
        'movimientos': movimientos,
    }
    return render(request, 'movimientos/list_mov_chofer.html', context)

####### Muestra Resumen Choferes en sesion #######
def movchofer(request):
    # Obtiene el chofer asociado al usuario autenticado
    chofer = request.user.chofer

    # Fecha de inicio y fin del mes actual
    today = now().date()
    start_of_month = today.replace(day=1)
    end_of_month = (start_of_month + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    # Total de kilómetros realizados por el chofer
    total_km = Movimientos.objects.filter(chofer=chofer).aggregate(
        total_km=Sum(F('kmFin') - F('kmInicio'))
    )['total_km'] or 0
    
    # Total de movimientos realizados por el chofer
    total_movimientos = Movimientos.objects.filter(chofer=chofer).count()

    # Total de registros realizados por el chofer
    registros_por_chofer = Movimientos.objects.filter(chofer=chofer).values('chofer').annotate(
        total_registros=Count('mov_id')
    ).order_by('-total_registros')
    
    # Kilómetros realizados por tipo de kilómetro y por mes
    km_por_tipo = Movimientos.objects.filter(
        chofer=chofer,
        fin__range=[start_of_month, end_of_month]  # Filtrar por el mes actual
    ).values('tipo_kilometro__descripcion').annotate(
        total_km=Sum(F('kmFin') - F('kmInicio'))
    ).order_by('tipo_kilometro__descripcion')

    # Cálculo directo de kilómetros normales y 100%
    km_normales = Movimientos.objects.filter(
        chofer=chofer,
        fin__range=[start_of_month, end_of_month],
        tipo_kilometro__descripcion='Normal'
    ).aggregate(total_km=Sum(F('kmFin') - F('kmInicio')))['total_km'] or 0

    km_100 = Movimientos.objects.filter(
        chofer=chofer,
        fin__range=[start_of_month, end_of_month],
        tipo_kilometro__descripcion='100%'
    ).aggregate(total_km=Sum(F('kmFin') - F('kmInicio')))['total_km'] or 0
    
    context = {
        'total_km': total_km,
        'registros_por_chofer': registros_por_chofer,
        'total_movimientos': total_movimientos,
        'km_normales': km_normales,
        'km_100': km_100,
        'km_por_tipo': km_por_tipo,  # Añadir esto si deseas mostrar km_por_tipo en la plantilla
    }
    return render(request, 'movimientos/movchofer.html', context)

####### Muestra Resumen de todos los Choferes #######
def movimiento(request):
    # Total de kilómetros realizados
    total_km = Movimientos.objects.aggregate(total_km=Sum(F('kmFin') - F('kmInicio')))['total_km']
    
    # Total de movimientos
    total_movimientos = Movimientos.objects.count()

    # Total de choferes que realizaron registros
    total_choferes = Movimientos.objects.values('chofer').distinct().count()
    
    # Total de registros realizados por chofer
    registros_por_chofer = Movimientos.objects.values('chofer').annotate(total_registros=Count('mov_id')).order_by('-total_registros')
    
    # Total de kilómetros por tipo
    km_por_tipo = Movimientos.objects.values('tipo_kilometro__descripcion').annotate(total_km=Sum(F('kmFin') - F('kmInicio'))).order_by('-total_km')
    
    context = {
        'total_km': total_km,
        'total_choferes': total_choferes,
        'registros_por_chofer': registros_por_chofer,
        'total_movimientos': total_movimientos,
        'km_por_tipo': km_por_tipo,
    }
    return render(request, 'movimientos/movimiento.html', context)

####### Funcion para determinar moviento por Chofer #######
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

####### Lista los campos del Chofer #######
def listusuariochofer(request):
    usuarioschofer = Chofer.objects.all()
    context = {
        'usuarioschofer': usuarioschofer,
    }
    return render(request, 'chofer/listusuariochofer.html', context)

######### Funciones para Graficos #######
@login_required
def kpi(request):

# <------------ Obtener el mes actual y el año actual ------------>
    fecha_actual = date.today()
    mes_actual = fecha_actual.month
    anio_actual = fecha_actual.year
    # Obtener los datos de tipos de kilómetros registrados en el mes actual
    datos_km_tipos = Movimientos.objects.filter(
        fin__year=anio_actual,
        fin__month=mes_actual
    ).values('tipo_kilometro__descripcion').annotate(
        total_km=Sum(F('kmFin') - F('kmInicio'))
    ).order_by('tipo_kilometro__descripcion')
    # Preparar las etiquetas y los datos para la gráfica
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

    # Crear un diccionario para traducir nombres de meses a castellano
    meses_en_castellano = {
        1: 'Ene', 2: 'Feb', 3: 'Mar', 4: 'Abr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Ago', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dic'
    }

    labels_meses = []
    series_meses = []

    for dato in datos_por_mes:
        mes_fecha = dato['mes']
        mes_nombre = meses_en_castellano[mes_fecha.month]  # Obtiene el nombre del mes en castellano
        anio = mes_fecha.year
        labels_meses.append(f'{mes_nombre} {anio}')  # Formatea como "Mes Año"
        series_meses.append(dato['total_km'])

# <------------ Obtener los datos de kilómetros por chofer ------------>
    choferes = Chofer.objects.all()
    labels_choferes = []
    series_choferes = []

    for chofer in choferes:
        labels_choferes.append(chofer.apellido)
        
        # Filtrar movimientos que tienen kmInicio y kmFin no nulos
        km_total = Movimientos.objects.filter(
            chofer=chofer,
            kmInicio__isnull=False,
            kmFin__isnull=False
        ).aggregate(
            total_km=Sum(ExpressionWrapper(F('kmFin') - F('kmInicio'), output_field=IntegerField()))
        )['total_km']
        
        series_choferes.append(km_total or 0)  # Si no hay movimientos, km_total será None

# <------------ Contar usuarios por rol ------------>
    usuarios_por_tipo = Usuario.objects.values('role').annotate(count=Count('id'))
    roles = ['chofer', 'admin']  # verifacar  eleonombres a los roles reales que tienes
    # Inicializar los conteos en 0
    conteos = {rol: 0 for rol in roles}
    # Contar usuarios por rol
    for item in usuarios_por_tipo:
        rol = item['role']
        conteos[rol] = item['count']
    # Preparar los datos para el gráfico
    labels_tipo = list(conteos.keys())
    series_tipo = list(conteos.values())

# <------------ Documentacion Vencida ------------>

    # Definir el rango de fecha (hoy + 30 días)
    hoy = datetime.today()
    fecha_limite = hoy + timedelta(days=30)

    # Filtrar las licencias que están vencidas y las que no lo están
    licencias_vencidas = Chofer.objects.filter(licencia_venc__lte=hoy).count()
    licencias_no_vencidas = Chofer.objects.filter(licencia_venc__gt=hoy).count()

    # Preparar los datos para el gráfico de pie
    labels_licencias = ['Vencidas', 'No Vencidas']
    series_licencias = [licencias_vencidas, licencias_no_vencidas]

    # Contexto para el template
    context = {
        'labels_licencias': labels_licencias,
        'series_licencias': series_licencias,
    }

# <------------ Vecimimientos por tipo de Documentacion ------------>
    # Definir el rango de fecha (hoy + 30 días)
    hoy = datetime.today()
    fecha_limite = hoy + timedelta(days=30)

    # Filtrar los registros con vencimientos mayores a hoy y menores a 30 días
    vencimientos = Chofer.objects.filter(
        Q(ingresoFCA_venc__gt=hoy, ingresoFCA_venc__lte=fecha_limite) |  # Es una función que permite construir consultas complejas y combinarlas usando operadores lógicos en este caso OR
        Q(licencia_venc__gt=hoy, licencia_venc__lte=fecha_limite) |
        Q(psicofisico_venc__gt=hoy, psicofisico_venc__lte=fecha_limite) |
        Q(curso_venc__gt=hoy, curso_venc__lte=fecha_limite)
    )

    # Contar los vencimientos por tipo de documentación
    conteo_vencimientos = {
        'Ingreso FCA': vencimientos.filter(ingresoFCA_venc__gt=hoy, ingresoFCA_venc__lte=fecha_limite).count(),
        'Licencia': vencimientos.filter(licencia_venc__gt=hoy, licencia_venc__lte=fecha_limite).count(),
        'Psicofísico': vencimientos.filter(psicofisico_venc__gt=hoy, psicofisico_venc__lte=fecha_limite).count(),
        'Curso': vencimientos.filter(curso_venc__gt=hoy, curso_venc__lte=fecha_limite).count(),
    }

    # Preparar los datos para el gráfico
    labels_vencimientos = list(conteo_vencimientos.keys())
    series_vencimientos = list(conteo_vencimientos.values())

#  <----------- Variables para Graficos ------------>
    context = {
        'labels_choferes': labels_choferes,
        'series_choferes': series_choferes,
        'labels_meses': labels_meses,
        'series_meses': series_meses,
        'labels_tipo': labels_tipo,
        'series_tipo': series_tipo,
        'labels_km_tipos': labels_km_tipos,
        'series_km_tipos': series_km_tipos,
        'labels_licencias': labels_licencias,
        'series_licencias': series_licencias,
        'labels_vencimientos': labels_vencimientos,
        'series_vencimientos': series_vencimientos,
    }
    return render(request, 'movimientos/analitica.html', context)
    
