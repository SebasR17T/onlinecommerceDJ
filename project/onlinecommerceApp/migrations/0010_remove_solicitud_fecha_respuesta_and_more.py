# Generated by Django 5.1 on 2024-08-29 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecommerceApp', '0009_remove_solicitud_id_usuario_modificacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='fecha_respuesta',
        ),
        migrations.RemoveField(
            model_name='solicitud',
            name='respuesta_cierre',
        ),
        migrations.AddField(
            model_name='solicitud',
            name='correo',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='telefono',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='descripcion',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
