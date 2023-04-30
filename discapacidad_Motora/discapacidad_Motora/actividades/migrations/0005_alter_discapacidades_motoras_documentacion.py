# Generated by Django 4.2 on 2023-04-28 18:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0004_alter_actividad_competencias_desarrollar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discapacidades_motoras',
            name='documentacion',
            field=models.FileField(blank=True, null=True, upload_to='Documentos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'], message='Sólo se permiten Documentos PDF')]),
        ),
    ]