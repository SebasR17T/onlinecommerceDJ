from django.db import migrations

CATEGORIAS_DEFAULT = [
    'Moda y Ropa',
    'Calzado',
    'Accesorios',
    'Relojes y Joyería',
    'Tecnología',
    'Hogar y Decoración',
    'Alimentos y Bebidas',
    'Belleza y Cuidado Personal',
    'Deportes',
    'Automóviles',
]


def crear_categorias_default(apps, schema_editor):
    CategoriaTienda = apps.get_model('onlinecommerceApp', 'CategoriaTienda')
    for nombre in CATEGORIAS_DEFAULT:
        CategoriaTienda.objects.get_or_create(nombre=nombre)


def eliminar_categorias_default(apps, schema_editor):
    CategoriaTienda = apps.get_model('onlinecommerceApp', 'CategoriaTienda')
    CategoriaTienda.objects.filter(nombre__in=CATEGORIAS_DEFAULT).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecommerceApp', '0017_usuario_session_key'),
    ]

    operations = [
        migrations.RunPython(crear_categorias_default, eliminar_categorias_default),
    ]
