# Generated by Django 4.2.6 on 2023-11-27 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0015_rename_imagen_dispostivo_dispositivo_imagen_dispositivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='imagen_dispositivo',
            field=models.ImageField(blank=True, null=True, upload_to='datos/dispositivos/', verbose_name='My image'),
        ),
    ]
