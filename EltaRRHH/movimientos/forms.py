from django import forms
from .models import Movimientos, TipoKilometros


class MovimientosForm(forms.ModelForm):
    
        TipoKilometros = (
                ('1', 'Km Normales'),
                ('2', 'Km al 100%'),
                ('3', 'Km al 100% - 1.2'),
        )
    
        nFlota = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Ingrese Número de Flota',
            'class': 'form-control',
        }))
        inicio = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
            'placeholder': 'Fecha y Hora de Inicio',
            'class': 'form-control',
            'type': 'datetime-local'
        }))
        fin = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
            'placeholder': 'Fecha y Hora de Fin',
            'class': 'form-control',
            'type': 'datetime-local'
        }), required=False)
        kmInicio = forms.IntegerField(widget=forms.NumberInput(attrs={
            'placeholder': 'Kilómetros Iniciales',
            'class': 'form-control',
        }))
        kmFin = forms.IntegerField(widget=forms.NumberInput(attrs={
            'placeholder': 'Kilómetros Finales',
            'class': 'form-control',
        }), required=False)
        lugar_inicio = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Lugar de Inicio',
            'class': 'form-control',
        }))
        lugar_fin = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Lugar de Fin',
            'class': 'form-control',
        }), required=False)
        
        tipo_kilometro = forms.ChoiceField(choices=TipoKilometros, widget=forms.Select(attrs={
                'class': 'form-control',
        }))
        lleva_carga = forms.BooleanField(widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        }), required=False)
        permanencia = forms.BooleanField(widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        }), required=False)
        diasPermanencia = forms.IntegerField(widget=forms.NumberInput(attrs={
            'placeholder': 'Días de Permanencia',
            'class': 'form-control',
        }), required=False)
        cruce_frontera = forms.BooleanField(widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        }), required=False)
        comentarios = forms.CharField(widget=forms.Textarea(attrs={
            'placeholder': 'Comentarios',
            'class': 'form-control',
        }), required=False)





class MovimientosForm(forms.ModelForm):
    tipo_kilometro = forms.ModelChoiceField(queryset=TipoKilometros.objects.all())


class MovimientosForm(forms.ModelForm):
    class Meta:
        model = Movimientos
        fields = [
            'nFlota', 'inicio', 'fin', 'kmInicio', 'kmFin', 'lugar_inicio', 
            'lugar_fin', 'tipo_kilometro', 'lleva_carga', 'permanencia', 
            'diasPermanencia', 'cruce_frontera', 'comentarios'
        ]
        widgets = {
            'inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'fin': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'nFlota': forms.TextInput(attrs={'class': 'form-control'}),
            'kmInicio': forms.NumberInput(attrs={'class': 'form-control'}),
            'kmFin': forms.NumberInput(attrs={'class': 'form-control'}),
            'lugar_inicio': forms.TextInput(attrs={'class': 'form-control'}),
            'lugar_fin': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_kilometro': forms.Select(attrs={'class': 'form-control'}),
            'lleva_carga': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'permanencia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'diasPermanencia': forms.NumberInput(attrs={'class': 'form-control'}),
            'cruce_frontera': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control'}),
        }