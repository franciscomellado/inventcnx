# Generated by Django 4.2.6 on 2023-12-11 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licencias', '0016_remove_licencia_disponible_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='licencia',
            name='disponible',
        ),
    ]
