# Generated by Django 4.2.6 on 2023-12-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licencias', '0005_alter_licencia_fecha_vencimiento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='licenciausuario',
            old_name='licencias',
            new_name='licencia',
        ),
        migrations.AlterUniqueTogether(
            name='licenciausuario',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='licenciausuario',
            constraint=models.UniqueConstraint(fields=('persona', 'licencia'), name='unique licencia'),
        ),
    ]
