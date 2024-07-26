from django import forms
from .models import Movimientos, TipoKilometros

class MovimientosForm(forms.ModelForm):
    tipo_kilometro = forms.ModelChoiceField(queryset=TipoKilometros.objects.all())

    class Meta:
        model = Movimientos
        fields = ['nFlota', 'inicio', 'fin', 'kmInicio', 'kmFin', 'lugar_inicio', 
                    'lugar_fin', 'tipo_kilometro', 'lleva_carga', 'permanencia', 
                    'diasPermanencia', 'cruce_frontera', 'comentarios']