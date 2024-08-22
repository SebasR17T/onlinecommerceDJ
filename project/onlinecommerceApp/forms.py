from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CrearUsuarioForm(UserCreationForm):
    ROLE_CHOICES = (
        ('comprador', 'Comprador'),
        ('tendero', 'Tendero'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Rol')

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2', 'role', 'apellido']



class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput
    )
