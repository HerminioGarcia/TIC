# Generated by Django 4.2.1 on 2023-05-05 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0002_alter_discapacidades_motoras_documentacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discapacidades_motoras',
            old_name='documentacion',
            new_name='documentaciones',
        ),
    ]