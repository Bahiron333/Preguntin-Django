# Generated by Django 5.0.11 on 2025-01-22 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Juego', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preguntas',
            name='Nombre_pregunta',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='Opcion_A',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='Opcion_B',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='Opcion_C',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='preguntas',
            name='Opcion_D',
            field=models.CharField(max_length=100),
        ),
    ]
