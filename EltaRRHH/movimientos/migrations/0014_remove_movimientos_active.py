# Generated by Django 5.0.6 on 2024-08-02 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0013_alter_movimientos_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimientos',
            name='active',
        ),
    ]
