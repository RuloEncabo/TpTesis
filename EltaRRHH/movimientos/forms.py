from django import forms
from .models import Movimiento,TipoKilometro

class MovimientoForm(forms.ModelForm):
    tipo_kilometro = forms.ModelChoiceField(queryset=TipoKilometro.objects.all())

    class Meta:
        model = Movimiento
        fields = ['nFlota', 'inicio', 'fin', 'kmInicio', 'kmFin', 'lugar_inicio', 
                    'lugar_fin', 'tipo_kilometro', 'lleva_carga', 'permanencia', 
                    'diasPermanencia', 'cruce_frontera', 'comentarios']