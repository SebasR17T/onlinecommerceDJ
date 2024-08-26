
# Register your models here.
from django.contrib import admin
from .models import Usuario, CategoriaTienda
from .models import CategoriaProducto

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'apellido', 'telefono', 'fecha_nacimiento', 'cedula', 'tipo_cedula', 'genero', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'apellido')

admin.site.register(Usuario, UsuarioAdmin)




@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre')
    search_fields = ('nombre',)

@admin.register(CategoriaTienda)
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre')
    search_fields = ('nombre',)