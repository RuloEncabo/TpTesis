from django.shortcuts import render, redirect
from .forms import ChoferForm
from .models import Chofer

def registrar_chofer(request):
    if request.method == 'POST':
        form = ChoferForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('alguna_vista_de_exito')  # Redirigir a una vista de éxito
    else:
        form = ChoferForm()
    return render(request, 'chofer/rregChofer.html', {'form': form})