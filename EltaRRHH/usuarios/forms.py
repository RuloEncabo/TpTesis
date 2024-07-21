from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
        
        first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese Nombre',
        'class': 'form-control',
        }))
        last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese Apellido',
        'class': 'form-control',
        }))
        phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese Celular',
        'class': 'form-control',
        }))
        password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese Clave',
        'class': 'form-control',
        }))
        email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Ingrese E-Mail',
        'class': 'form-control',
        }))
        confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar Clave',
        'class': 'form-control',
        }))

        class Meta:
                model = Usuario  # Aquí se especifica el modelo asociado
                fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

        def clean(self):
                cleaned_data = super(RegistroForm, self).clean()
                password = cleaned_data.get('password')
                confirm_password = cleaned_data.get('confirm_password')
        
                if password != confirm_password:
                        raise forms.ValidationError(
                        "Las contraseñas no coinciden"
                )