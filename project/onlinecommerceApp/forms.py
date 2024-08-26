from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Tienda, Inventario, Carrito
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
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'descripcion', 'precio', 'fecha_vencimiento', 'id_categoria_producto', 'imagen']




class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = ['nombre', 'telefono', 'descripcion', 'correo', 'instagram', 'id_categoria', 'id_direccion', 'imagen']



class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['id_producto', 'cantidad']



