from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'role']

class UsuarioChangeForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'role']