# Generated by Django 5.0.3 on 2024-07-28 11:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0002_alter_movimientos_tipo_kilometro'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimientos',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movimientos',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
