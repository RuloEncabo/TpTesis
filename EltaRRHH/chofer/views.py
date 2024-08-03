from datetime import date
from django.shortcuts import get_object_or_404, render, redirect
from .forms import ChoferForm
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
def modidoc(request, id):
    chofer = get_object_or_404(Chofer, id=id)

    if request.method == 'POST':
        form = ChoferForm(request.POST, instance=chofer)
        if form.is_valid():
            form.save()
            return redirect('listdoc')  # Redirige a la lista después de guardar
    else:
        form = ChoferForm(instance=chofer)

    return render(request, 'chofer/modidoc.html', {'form': form, 'chofer': chofer})

"""
def registro_chofer(request):
    if request.method == 'POST':
        form = ChoferForm(request.POST)
        chofer_form = ChoferForm(request.POST, request.FILES)
        if form.is_valid() and chofer_form.is_valid():
            email = form.cleaned_data['email']
            
            user, created = Usuario.objects.get_or_create(
                email=email,
                defaults={
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'username': email.split("@")[0],
                    'phone_number': form.cleaned_data['phone_number'],
                    'password': form.cleaned_data['password']
                }
            )
            
            if created:
                # Crear el chofer solo si el usuario es nuevo
                chofer = chofer_form.save(commit=False)
                chofer.usuario = user
                chofer.save()

                # Iniciar sesión automáticamente
                login(request, user)

                # Redirigir a una página de éxito
                return redirect('success_page')  # Cambia 'success_page' por la URL adecuada
            else:
                # El usuario ya existe, no necesitas guardar los datos personales
                chofer = chofer_form.save(commit=False)
                chofer.usuario = user
                chofer.save()
                
                # Redirigir o mostrar un mensaje que indique que el usuario ya está registrado
                return redirect('success_page')  # Cambia 'success_page' por la URL adecuada

    else:
        form = ChoferForm()
        chofer_form = ChoferForm()

    context = {
        'form': form,
        'chofer_form': chofer_form,
        'user_exists': False
    }

    # Verifica si el usuario ya existe basándote en el correo electrónico
    if request.method == 'POST':
        email = request.POST.get('email')
        if email and Usuario.objects.filter(email=email).exists():
            context['user_exists'] = True

    return render(request, 'chofer/regChoferistro.html', context)
"""
