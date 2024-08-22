# Generated by Django 5.1 on 2024-08-21 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
            name='Imagenes',
            fields=[
                ('id_imagen', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_archivo', models.CharField(blank=True, max_length=30, null=True)),
                ('ruta_archivo', models.CharField(blank=True, max_length=70, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
                ('titulo', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('fecha_modificacion', models.DateField(blank=True, null=True)),
                ('formato', models.CharField(blank=True, max_length=40, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('etiquetas', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'imagenes',
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
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('fecha_entrega', models.DateField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('estado', models.CharField(blank=True, max_length=250, null=True)),
                ('total', models.IntegerField(blank=True, null=True)),
                ('tipo_entrega', models.CharField(blank=True, max_length=13, null=True)),
            ],
            options={
                'db_table': 'pedido',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'rol',
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
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('correo', models.CharField(max_length=300)),
                ('contrasena', models.CharField(max_length=200)),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('fecha_modificacion', models.DateField(blank=True, null=True)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('cedula', models.IntegerField(blank=True, null=True)),
                ('tipo_cedula', models.CharField(blank=True, max_length=30, null=True)),
                ('genero', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'usuario',
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
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.DecimalField(decimal_places=3, max_digits=10)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('fecha_modificado', models.DateField(blank=True, null=True)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('id_categoria_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.categoriaproducto')),
                ('id_imagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.imagenes')),
                ('id_usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_creado', to='onlinecommerceApp.usuario')),
                ('id_usuario_modificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_modificado', to='onlinecommerceApp.usuario')),
            ],
            options={
                'db_table': 'producto',
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
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.usuario')),
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
                ('id_tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.tienda')),
                ('id_tipo_solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.tiposolicitud')),
                ('id_usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_creada', to='onlinecommerceApp.usuario')),
                ('id_usuario_modificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_modificada', to='onlinecommerceApp.usuario')),
                ('id_usuario_respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitud_respondida', to='onlinecommerceApp.usuario')),
            ],
            options={
                'db_table': 'solicitud',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='pedido',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.usuario'),
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
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.pedido')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.usuario')),
            ],
            options={
                'db_table': 'pagos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.CharField(max_length=45)),
                ('fecha_creacion', models.DateField(blank=True, null=True)),
                ('fecha_modificado', models.DateField(blank=True, null=True)),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.producto')),
                ('id_tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.tienda')),
                ('id_usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario_creado', to='onlinecommerceApp.usuario')),
                ('id_usuario_modificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario_modificado', to='onlinecommerceApp.usuario')),
            ],
            options={
                'db_table': 'inventario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='InteraccionSolicitud',
            fields=[
                ('id_interaccion', models.AutoField(primary_key=True, serialize=False)),
                ('deleted', models.BooleanField(default=False)),
                ('interaccion', models.CharField(blank=True, max_length=300, null=True)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_creacion', models.DateField()),
                ('id_usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.usuario')),
            ],
            options={
                'db_table': 'interaccion_solicitud',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='imagenes',
            name='usuario_creacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.usuario'),
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
                ('id_direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.direccion')),
                ('id_pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.pedido')),
                ('id_usuario_domiciliario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.usuario')),
            ],
            options={
                'db_table': 'detalle_domicilio',
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
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.producto')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.usuario')),
            ],
            options={
                'db_table': 'carrito',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UsuarioHasRol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.rol')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.usuario')),
            ],
            options={
                'db_table': 'usuario_has_rol',
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
                ('id_usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecommerceApp.usuario')),
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
