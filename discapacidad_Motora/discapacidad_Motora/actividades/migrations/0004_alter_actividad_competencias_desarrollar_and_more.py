# Generated by Django 4.2 on 2023-04-28 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0003_remove_actividad_descripcion_actividad_recursos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='competencias_desarrollar',
            field=models.TextField(blank=True, null=True, verbose_name='Competencias a desarrollar:'),
        ),
        migrations.AlterField(
            model_name='discapacidades_motoras',
            name='documentacion',
            field=models.FileField(blank=True, null=True, upload_to='Documentos'),
        ),
    ]
