# Generated by Django 5.1 on 2024-08-28 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecommerceApp', '0006_alter_carrito_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitud',
            name='id_pedido',
        ),
    ]
