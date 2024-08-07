from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Chofer

class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = [
            'nombre', 'apellido', 'dni', 'calle', 'nrocalle',
            'piso', 'departamento', 'barrio', 'localidad', 'provincia', 'cp', 'movil',
            'contactoemergencia', 'parentesco', 'foto', 'ingresoFCA_venc', 'licencia_venc',
            'psicofisico_venc', 'curso_venc'
        ]
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese Nombre', 'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Ingrese Apellido', 'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese DNI', 'class': 'form-control'}),
            'calle': forms.TextInput(attrs={'placeholder': 'Ingrese Calle', 'class': 'form-control'}),
            'nrocalle': forms.TextInput(attrs={'placeholder': 'Ingrese Número de Calle', 'class': 'form-control'}),
            'piso': forms.TextInput(attrs={'placeholder': 'Ingrese Piso', 'class': 'form-control'}),
            'departamento': forms.TextInput(attrs={'placeholder': 'Ingrese Departamento', 'class': 'form-control'}),
            'barrio': forms.TextInput(attrs={'placeholder': 'Ingrese Barrio', 'class': 'form-control'}),
            'localidad': forms.TextInput(attrs={'placeholder': 'Ingrese Localidad', 'class': 'form-control'}),
            'provincia': forms.TextInput(attrs={'placeholder': 'Ingrese Provincia', 'class': 'form-control'}),
            'cp': forms.NumberInput(attrs={'placeholder': 'Ingrese Código Postal', 'class': 'form-control'}),
            'movil': forms.TextInput(attrs={'placeholder': 'Ingrese Móvil', 'class': 'form-control'}),
            'contactoemergencia': forms.TextInput(attrs={'placeholder': 'Ingrese Contacto de Emergencia', 'class': 'form-control'}),
            'parentesco': forms.TextInput(attrs={'placeholder': 'Ingrese Parentesco', 'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'ingresoFCA_venc': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'licencia_venc': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'psicofisico_venc': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'curso_venc': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        
        
class ChoferVencimientoForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = ['ingresoFCA_venc', 'licencia_venc', 'psicofisico_venc', 'curso_venc']
        widgets = {
            'ingresoFCA_venc': forms.DateInput(attrs={'class': 'form-control'}),
            'licencia_venc': forms.DateInput(attrs={'class': 'form-control'}),
            'psicofisico_venc': forms.DateInput(attrs={'class': 'form-control'}),
            'curso_venc': forms.DateInput(attrs={'class': 'form-control'}),
        }
        
    