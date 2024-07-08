from django.shortcuts import render

# Create your views here.
def registro(request):
    return render(request, 'usuarios/registro.html')

def login(request):
    return render(request, 'usuarios/login.html')

def logout(request):
    return 