# Generated by Django 4.2.6 on 2023-11-29 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='usuario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]