# Generated by Django 5.0.3 on 2024-07-26 12:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0003_remove_usuariochofer_movil_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField()),
                ('fin', models.DateTimeField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('chofer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuariochofer')),
            ],
        ),
    ]