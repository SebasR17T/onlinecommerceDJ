# Generated by Django 5.1 on 2024-08-25 00:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecommerceApp', '0004_alter_inventario_id_usuario_creacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_usuario_modificacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producto_modificado', to=settings.AUTH_USER_MODEL),
        ),
    ]
