# Generated by Django 5.0.11 on 2025-01-22 04:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Usuario', models.CharField(max_length=30)),
                ('passworld', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='informacion_contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
                ('adress', models.CharField(max_length=30)),
                ('Id_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Jugador.usuario')),
            ],
        ),
    ]
