# Generated by Django 4.2.6 on 2023-11-26 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0009_inventario_fecha_caducidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='fecha_caducidad',
            new_name='fecha_caducidad_dispositivo',
        ),
    ]