# Generated by Django 5.0.3 on 2024-07-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_usuariochofer_movil_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='role',
            field=models.CharField(choices=[('admin', 'RRHH'), ('chofer', 'Chofer')], default='chofer', max_length=10),
        ),
    ]