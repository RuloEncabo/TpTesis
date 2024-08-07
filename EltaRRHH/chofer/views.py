from datetime import date
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ChoferForm,ChoferVencimientoForm
from .models import Chofer


####
def listchofer(request):
    choferes = Chofer.objects.all()
    
    # Calcular días restantes para cada fecha de vencimiento
    for chofer in choferes:
        chofer.dias_ingresoFCA_venc = (chofer.ingresoFCA_venc - date.today()).days
        chofer.dias_licencia_venc = (chofer.licencia_venc - date.today()).days
        chofer.dias_psicofisico_venc = (chofer.psicofisico_venc - date.today()).days
        chofer.dias_curso_venc = (chofer.curso_venc - date.today()).days

    context = {
        'choferes': choferes,
    }
    return render(request, 'chofer/listusuariochofer.html', context)

###  Funcion para listar los Vencimientos ###
def listdoc(request):
    choferes = Chofer.objects.all()
    
    # Calcular días restantes para cada fecha de vencimiento
    for chofer in choferes:
        chofer.dias_ingresoFCA_venc = (chofer.ingresoFCA_venc - date.today()).days
        chofer.dias_licencia_venc = (chofer.licencia_venc - date.today()).days
        chofer.dias_psicofisico_venc = (chofer.psicofisico_venc - date.today()).days
        chofer.dias_curso_venc = (chofer.curso_venc - date.today()).days

    context = {
        'choferes': choferes,
    }
    return render(request, 'chofer/listdoc.html', context)



###  Funcion para modificar los Vencimientos ###
def modidoc(request, chofer_id):
    chofer = get_object_or_404(Chofer, Id_chofer=chofer_id)

    if request.method == 'POST':
        form = ChoferVencimientoForm(request.POST, instance=chofer)
        if form.is_valid():
            form.save()
            print("Formulario guardado exitosamente")  # Debug
            return redirect('listdoc')  # Redirige a la lista después de guardar
        else:
            print("Formulario no es válido")  # Debug
            print(form.errors)  # Mostrar errores del formulario para depuración
    else:
        form = ChoferForm(instance=chofer)

    return render(request, 'chofer/modidoc.html', {'form': form, 'chofer': chofer})
