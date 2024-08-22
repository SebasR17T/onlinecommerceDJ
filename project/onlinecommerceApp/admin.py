
# Register your models here.
from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'apellido', 'telefono', 'fecha_nacimiento', 'cedula', 'tipo_cedula', 'genero', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'apellido')

admin.site.register(Usuario, UsuarioAdmin)