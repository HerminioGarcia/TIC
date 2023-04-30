# Generated by Django 4.2 on 2023-04-18 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreActividad', models.CharField(max_length=200, verbose_name='Nombre de la actividad')),
                ('descripcion', models.TextField()),
                ('url', models.URLField(max_length=500)),
                ('discapacidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Discapacidad', to='actividades.discapacidades_motoras')),
            ],
        ),
    ]