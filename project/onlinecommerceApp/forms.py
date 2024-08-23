from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import Producto

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

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Extraer el argumento 'user' de kwargs
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Producto
        fields = ['nombre_producto', 'descripcion', 'precio', 'fecha_vencimiento', 'id_categoria_producto', 'imagen']

    def save(self, commit=True):
        producto = super().save(commit=False)
        if not producto.pk:  # Si es una nueva instancia
            producto.id_usuario_creacion = self.user
        producto.id_usuario_modificacion = self.user
        if commit:
            producto.save()
        return producto