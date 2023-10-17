# Generated by Django 4.2.6 on 2023-10-17 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("personas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Estado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("estado", models.CharField(max_length=100)),
                ("desripcion", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Marca",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Proveedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("codigo", models.CharField(max_length=100)),
                ("contacto", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Software",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("version", models.CharField(max_length=100)),
                ("cantidad_licencias", models.IntegerField(default=0)),
                ("duracion", models.IntegerField(default=0)),
                ("fecha_compra", models.DateTimeField(verbose_name="Fecha de ingreso")),
                (
                    "fecha_caducidad",
                    models.DateTimeField(verbose_name="Feha de caducidad"),
                ),
                ("valor", models.FloatField()),
                (
                    "tipo_moneda",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("UF", "unidad de fomento"),
                            ("CL", "Peso Chileno"),
                            ("US", "Dolar Americano"),
                            ("AUD", "Dolar Autraliano"),
                            ("EU", "Euros"),
                        ],
                        default="CL",
                        help_text="Tipo de moneda",
                        max_length=30,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Inventario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "fecha_ingreso",
                    models.DateTimeField(verbose_name="Fecha de ingreso"),
                ),
                ("valor", models.FloatField()),
                ("numero_orden", models.CharField(max_length=80)),
                ("tipo", models.CharField(max_length=100)),
                ("disponible", models.BooleanField(default=False)),
                ("archivo", models.ImageField(upload_to="datos/")),
                (
                    "estado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventario.estado",
                    ),
                ),
                (
                    "nombre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="personas.cliente",
                    ),
                ),
                (
                    "proveedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventario.proveedor",
                    ),
                ),
                (
                    "software",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventario.software",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Dispositivo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dispositivo", models.CharField(max_length=100)),
                ("tipo", models.CharField(max_length=100)),
                ("observacion", models.TextField()),
                ("imei", models.CharField(max_length=100)),
                ("num_serie", models.CharField(max_length=100)),
                (
                    "estado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventario.estado",
                    ),
                ),
                (
                    "marca",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventario.marca",
                    ),
                ),
            ],
        ),
    ]
