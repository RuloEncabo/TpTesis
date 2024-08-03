from django import forms
from .models import Movimientos, TipoKilometros



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