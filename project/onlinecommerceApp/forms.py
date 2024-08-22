from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    ROLE_CHOICES = (
        ('comprador', 'Comprador'),
        ('tendero', 'Tendero'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Rol')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']
