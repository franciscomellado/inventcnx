# Generated by Django 4.2.6 on 2023-10-18 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventario", "0003_alter_software_duracion_alter_software_fecha_compra"),
    ]

    operations = [
        migrations.AlterField(
            model_name="software",
            name="fecha_caducidad",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="software",
            name="fecha_compra",
            field=models.DateField(blank=True, null=True),
        ),
    ]