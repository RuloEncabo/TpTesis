# Generated by Django 5.0.3 on 2024-07-28 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0008_alter_movimientos_chofer'),
        ('usuarios', '0004_alter_usuario_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientos',
            name='chofer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuarios.usuariochofer'),
        ),
    ]
