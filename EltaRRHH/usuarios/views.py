from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Usuario
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
# Create your views here.


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



def registro(request):
    form = RegistroForm()
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password= form.cleaned_data['password']
            #marcelo@elta.com.ar
            username= email.split("@")[0]
            user = Usuario.objects.create_user(first_name=first_name,last_name=last_name,email=email, phone_number=phone_number,username=username,password=password )
            user.phone_number = phone_number
            #se insserta en la BD
            user.save()
            
            #Activar al usuario
            current_site = get_current_site(request)
            mail_subject = 'por favor active su cuenta de ELTA'
            body = render_to_string ('usuarios/usr_verificacion_mail.html',{
                
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
                
            })
            to_email = email
            send_email = EmailMessage(mail_subject,body,to=[to_email])
            send_email.send()   
            
            
            
            #messages.success(request,'Se Registro el Usuario Exitosamente')
            return redirect('/usuarios/login/?command=verification&email='+email) #redirecciona a la pag de login con el valor de lo parametros 

    context={
        
        'form':form
        
    }
    #envia el diccionario context que tiene la estructura del formulario creado 
    return render(request, 'usuarios/registro.html',context)

def login(request):
    #verifico que el metodo es post
    if request.method == 'POST':
        
        email = request.POST['email']
        password = request.POST['password']
        
        #se llama a la funcion para autentificar
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
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

    
@login_required(login_url='login')
def listar(request):
    return render (request, 'usuarios/listar.html')