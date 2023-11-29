# Generated by Django 4.2.6 on 2023-11-27 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0012_rename_imagendispostivo_dispositivo_imagen_dispostivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dispositivo',
            name='imagen_dispostivo',
        ),
        migrations.AddField(
            model_name='inventario',
            name='imagen_dispostivo',
            field=models.ImageField(null=True, upload_to='datos/dispositivos/'),
        ),
    ]