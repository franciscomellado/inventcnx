# Generated by Django 4.2.6 on 2023-11-27 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0014_remove_inventario_imagen_dispostivo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dispositivo',
            old_name='imagen_dispostivo',
            new_name='imagen_dispositivo',
        ),
    ]