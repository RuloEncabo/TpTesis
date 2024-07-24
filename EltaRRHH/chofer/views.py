from django.shortcuts import render, redirect
from .forms import ChoferForm
from .models import Chofer

####
def listchofer(request):
    choferes = Chofer.objects.all().order_by('-date_joined')
    context = {
        'choferes': choferes,
    }
    return render(request, 'chofer/listchofer.html', context)

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
