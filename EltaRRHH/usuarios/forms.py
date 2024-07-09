from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario



#la funcion se crea el formulario desde djangp 
class RegistroForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder':'Ingrese Clave',
            'class':'form-control',   
    }))
    
    #campo para confirmar la contraseña 
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placehoder':'Confirmar Clave',
        'class':'form-control',
        }))

    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']
        
#aplicar los estilos a todas las cajas 
def __init__(self,*args,**kwargs):
    super(RegistroForm,self).__init__(*args,**kwargs)
    
    self.fields['first_name'].widget.attrs['placeholder'] = 'Ingrese Nombre'
    self.fields['last_name'].widget.attrs['placeholder'] = 'Ingrese Apellido'
    self.fields['phone_number'].widget.attrs['placeholder'] = 'Ingrese celular'
    self.fields['email'].widget.attrs['placeholder'] = 'Correo Electronico'
    #bucle para aplicar los estilos en las cajas de texto
    for field in self.fields:
        self.fields[field].widget.attrs['class'] = 'form-control' #se instancia a cada caja de texto
