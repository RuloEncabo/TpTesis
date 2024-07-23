from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
        ROLES = (
                ('admin', 'Administrador'),
                ('rrhh', 'RRHH'),
                ('chofer', 'Chofer'),
        )

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
        email = forms.CharField(widget=forms.EmailInput(attrs={
                'placeholder': 'Ingrese E-Mail',
                'class': 'form-control',
        }))
        password = forms.CharField(widget=forms.PasswordInput(attrs={
                'placeholder': 'Ingrese Clave',
                'class': 'form-control',
        }))
        confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
                'placeholder': 'Confirmar Clave',
                'class': 'form-control',
        }))
        role = forms.ChoiceField(choices=ROLES, widget=forms.Select(attrs={
                'class': 'form-control',
        }))
        legajo = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese Legajo',
                'class': 'form-control',
        }), required=False)
        dni = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese DNI',
                'class': 'form-control',
        }), required=False)
        calle = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese Calle',
                'class': 'form-control',
        }), required=False)
        nrocalle = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese Número de Calle',
                'class': 'form-control',
        }), required=False)
        piso = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese Piso',
                'class': 'form-control',
        }), required=False)
        departamento = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese Departamento',
                'class': 'form-control',
        }), required=False)
        barrio = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese Barrio',
                'class': 'form-control',
        }), required=False)
        localidad = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese Localidad',
                'class': 'form-control',
        }), required=False)
        provincia = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese Provincia',
                'class': 'form-control',
        }), required=False)
        cp = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese Código Postal',
                'class': 'form-control',
        }), required=False)
        contactoemergencia = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese Contacto de Emergencia',
                'class': 'form-control',
        }), required=False)
        parentesco = forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Ingrese Parentesco',
                'class': 'form-control',
        }), required=False)
        foto = forms.ImageField(required=False)
        ingresoFCA_venc = forms.DateField(widget=forms.DateInput(attrs={
                'placeholder': 'Ingrese Ingreso FCA Vencimiento',
                'class': 'form-control',
        }), required=False)
        licencia_venc = forms.DateField(widget=forms.DateInput(attrs={
                'placeholder': 'Ingrese Licencia Vencimiento',
                'class': 'form-control',
        }), required=False)
        psicofisico_venc = forms.DateField(widget=forms.DateInput(attrs={
                'placeholder': 'Ingrese Psicofísico Vencimiento',
                'class': 'form-control',
        }), required=False)
        curso_venc = forms.DateField(widget=forms.DateInput(attrs={
                'placeholder': 'Ingrese Curso Vencimiento',
                'class': 'form-control',
        }), required=False)

        class Meta:
                model = Usuario
                fields = ['first_name', 'last_name', 'phone_number', 'email', 'password', 'confirm_password', 'role', 'legajo', 'dni', 'calle', 'nrocalle', 'piso', 'departamento', 'barrio', 'localidad', 'provincia', 'cp', 'contactoemergencia', 'parentesco', 'foto', 'ingresoFCA_venc', 'licencia_venc', 'psicofisico_venc', 'curso_venc']

        def clean(self):
                cleaned_data = super(RegistroForm, self).clean()
                password = cleaned_data.get('password')
                confirm_password = cleaned_data.get('confirm_password')

                if password != confirm_password:
                        raise forms.ValidationError(
                        "Las contraseñas no coinciden"
                )