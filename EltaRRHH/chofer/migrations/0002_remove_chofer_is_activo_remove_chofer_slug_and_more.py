# Generated by Django 5.0.6 on 2024-07-12 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chofer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chofer',
            name='is_activo',
        ),
        migrations.RemoveField(
            model_name='chofer',
            name='slug',
        ),
        migrations.AddField(
            model_name='chofer',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
