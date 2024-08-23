# Generated by Django 5.0.7 on 2024-08-22 16:30

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'categoria_producto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CategoriaTienda',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'categoria_tienda',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.AutoField(primary_key=True, serialize=False)),
                ('barrio', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=100)),
                ('pais', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'direccion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id_metodo_pago', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.IntegerField()),
            ],
            options={
                'db_table': 'metodo_pago',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TipoSolicitud',
            fields=[
                ('id_tipo_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tipo_solicitud',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('apellido', models.CharField(max_length=200)),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('fecha_modificacion', models.DateField(blank=True, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('cedula', models.IntegerField(blank=True, null=True)),
                ('tipo_cedula', models.CharField(blank=True, max_length=30, null=True)),
                ('genero', models.CharField(blank=True, max_length=50, null=True)),
                ('imagen', models.CharField(max_length=250)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Usuario',
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='InteraccionSolicitud',
            fields=[
                ('id_interaccion', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False)),
                ('interaccion', models.CharField(blank=True, max_length=300, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateField()),
                ('id_usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'interaccion_solicitud',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('fecha_entrega', models.DateField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('estado', models.CharField(blank=True, max_length=250, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('tipo_entrega', models.CharField(blank=True, max_length=13, null=True)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'pedido',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id_pagos', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_pago', models.DateField(blank=True, null=True)),
                ('monto_pago', models.IntegerField(blank=True, null=True)),
                ('moneda', models.CharField(blank=True, max_length=50, null=True)),
                ('estado_pago', models.IntegerField(blank=True, null=True)),
                ('detalle_pago', models.CharField(blank=True, max_length=50, null=True)),
                ('id_metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.metodopago')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.pedido')),
            ],
            options={
                'db_table': 'pagos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetalleFisico',
            fields=[
                ('id_fisico', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_recoger_inicio', models.DateField(blank=True, null=True)),
                ('fecha_recoger_fin', models.DateField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.pedido')),
            ],
            options={
                'db_table': 'detalle_fisico',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='DetalleDomicilio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_hora_pedido_listo', models.DateTimeField()),
                ('fecha_hora_pedido_recogido', models.DateTimeField()),
                ('fecha_hora_pedido_entrega', models.DateTimeField()),
                ('estado', models.CharField(max_length=50)),
                ('novedades', models.CharField(blank=True, max_length=250, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id_usuario_domiciliario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.direccion')),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.pedido')),
            ],
            options={
                'db_table': 'detalle_domicilio',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('fecha_modificado', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('imagen', models.CharField(max_length=250)),
                ('id_categoria_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.categoriaproducto')),
                ('id_usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_creado', to=settings.AUTH_USER_MODEL)),
                ('id_usuario_modificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_modificado', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'producto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id_carrito', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateField()),
                ('deleted', models.BooleanField(default=False)),
                ('estado_carrito', models.CharField(max_length=50)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.producto')),
            ],
            options={
                'db_table': 'carrito',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductoHasPedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False)),
                ('precio_unitario', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.IntegerField(blank=True, null=True)),
                ('subtotal', models.IntegerField(blank=True, null=True)),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.pedido')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.producto')),
            ],
            options={
                'db_table': 'producto_has_pedido',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id_tienda', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('descripcion', models.CharField(blank=True, max_length=500, null=True)),
                ('correo', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('fecha_modificacion', models.DateField(blank=True, null=True)),
                ('imagen', models.CharField(max_length=250)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.categoriatienda')),
                ('id_direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.direccion')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tienda',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_tienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.tienda'),
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.CharField(max_length=45)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('fecha_modificado', models.DateField(blank=True, null=True)),
                ('id_usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario_creado', to=settings.AUTH_USER_MODEL)),
                ('id_usuario_modificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario_modificado', to=settings.AUTH_USER_MODEL)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.producto')),
                ('id_tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.tienda')),
            ],
            options={
                'db_table': 'inventario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id_solicitud', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_solicitud', models.DateField()),
                ('estado', models.CharField(max_length=50)),
                ('fecha_respuesta', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=300, null=True)),
                ('asunto', models.CharField(blank=True, max_length=250, null=True)),
                ('respuesta_cierre', models.CharField(blank=True, max_length=250, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.pedido')),
                ('id_usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_creada', to=settings.AUTH_USER_MODEL)),
                ('id_usuario_modificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_modificada', to=settings.AUTH_USER_MODEL)),
                ('id_usuario_respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_respondida', to=settings.AUTH_USER_MODEL)),
                ('id_tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.tienda')),
                ('id_tipo_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.tiposolicitud')),
            ],
            options={
                'db_table': 'solicitud',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id_venta', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateField()),
                ('total', models.IntegerField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('id_metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.metodopago')),
                ('id_tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.tienda')),
                ('id_usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ventas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductoHasVenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('precio_unitario', models.FloatField(blank=True, null=True)),
                ('catidad', models.IntegerField(blank=True, null=True)),
                ('subtotal', models.FloatField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.producto')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.ventas')),
            ],
            options={
                'db_table': 'producto_has_venta',
                'managed': True,
            },
        ),
    ]
