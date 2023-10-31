# Generated by Django 4.2.6 on 2023-10-30 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('inventario', '0002_remove_dispositivo_factura_remove_software_factura_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'inventario'), ('model', 'dispositivo')), models.Q(('app_label', 'inventario'), ('model', 'software')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='object_id',
            field=models.PositiveIntegerField(),
        ),
    ]