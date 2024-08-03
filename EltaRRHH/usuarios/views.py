import email
from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Usuario, UsuarioChofer
from chofer.models import Chofer 
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def is_admin(user):
    return user.role == 'admin'

def is_chofer(user):
    return user.role == 'chofer'

#acceso Web administracion
@login_required(login_url='login')
@user_passes_test(is_admin)
def admin(request):
    return render(request, 'home.html')

#acceso Web Choferes
@login_required(login_url='login')
@user_passes_test(is_chofer)
def chofer(request):
    return render(request, 'hchofer.html')

### Funcion para Registrar usuario o UsuarioChofer ###
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                email = form.cleaned_data['email']
                # Crear el usuario
                user = Usuario.objects.create_user(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    phone_number=form.cleaned_data['phone_number'],
                    email=email,
                    password=form.cleaned_data['password'],
                    role=form.cleaned_data['role'],
                    username=email.split("@")[0]
                )
                
                # Si el rol es chofer, crear instancia de Chofer
                if form.cleaned_data['role'] == 'chofer':
                    Chofer.objects.create(
                        usuario=user,
                        nombre=form.cleaned_data['first_name'],
                        apellido=form.cleaned_data['last_name'],
                        dni=form.cleaned_data['dni'],
                        calle=form.cleaned_data['calle'],
                        nrocalle=form.cleaned_data['nrocalle'],
                        piso=form.cleaned_data['piso'],
                        departamento=form.cleaned_data['departamento'],
                        barrio=form.cleaned_data['barrio'],
                        localidad=form.cleaned_data['localidad'],
                        provincia=form.cleaned_data['provincia'],
                        cp=form.cleaned_data['cp'],
                        movil=form.cleaned_data['phone_number'],
                        contactoemergencia=form.cleaned_data['contactoemergencia'],
                        parentesco=form.cleaned_data['parentesco'],
                        foto=form.cleaned_data['foto'],
                        ingresoFCA_venc=form.cleaned_data['ingresoFCA_venc'],
                        licencia_venc=form.cleaned_data['licencia_venc'],
                        psicofisico_venc=form.cleaned_data['psicofisico_venc'],
                        curso_venc=form.cleaned_data['curso_venc']
                    )
                    
                # Enviar correo de activación
                current_site = get_current_site(request)
                mail_subject = 'Por favor, active su cuenta de ELTA'
                body = render_to_string('usuarios/usr_verificacion_mail.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = email
                send_email = EmailMessage(mail_subject, body, to=[to_email])
                send_email.send()
                
                messages.success(request, 'Se ha registrado el usuario exitosamente. Por favor, verifica tu email para activar tu cuenta.')
                return redirect('/usuarios/login/?command=verification&email=' + email)

            except IntegrityError as e:
                form.add_error(None, "Error al crear el usuario. Por favor, intente nuevamente.")
            except Exception as e:
                form.add_error(None, f"Error inesperado: {str(e)}")
    else:
        form = RegistroForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})


### Funcion para Login ###
def login(request):
    #verifico que el metodo es post
    if request.method == 'POST':
        
        email = request.POST['email']
        password = request.POST['password']
        
        #se llama a la funcion para autentificar
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            #messages.successs (request, " Has iniciado la sesion exitosamente")
            if user.role == 'admin':
                return redirect('home')
            elif user.role == 'chofer':
                return redirect('chofer')
            else:
                return redirect('login')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')
    
    
    return render(request, 'usuarios/login.html')

#####
@login_required(login_url='login')
def logout(request):
    
    auth.logout(request)
    messages.success(request, 'Sesion Cerrada')
    
    return redirect('login')

#FUNCION PARA ACTIVAR EL USUARIO
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Usuario.objects.get(pk=uid)
    
    except(TypeError, ValueError, OverflowError, Usuario.DoesNotExist):
        user = None
    #se activa el usuario 
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Tu Usuario se a activado Exitosamente !!!')
        return redirect('login')
    else:
        messages.error(request, 'Tu Usuario NO se Activó !!!')
        return redirect('registro')
####    
@login_required(login_url='login')
def listar(request):
    return render (request, 'usuarios/listar.html')

####
def listusuario(request):
    usuarios = Usuario.objects.all().order_by('-date_joined')
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'usuarios/listusuario.html', context)

### Lista los campos del Chofer ###
def listusuariochofer(request):
    usuarioschofer = UsuarioChofer.objects.all()
    context = {
        'usuarioschofer': usuarioschofer,
    }
    return render(request, 'usuarios/listusuariochofer.html', context)