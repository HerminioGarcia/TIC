# Generated by Django 4.2 on 2023-04-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0006_remove_actividad_tempo'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='tempo',
            field=models.IntegerField(default=0),
        ),
    ]
