from django.shortcuts import render
from .forms import RegistroForm
# Create your views here.

def registro(request):

    form = RegistroForm()

    context={
        
        'form':form
        
    }
    #envia el diccionario context que tiene la estructura del formulario creado 
    return render(request, 'usuarios/registro.html',context)

def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    return 