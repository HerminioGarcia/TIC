# Generated by Django 4.2 on 2023-04-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discapacidades_motoras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDisapacidad', models.CharField(max_length=200, verbose_name='Nombre del la discapacidad')),
                ('descripcion', models.TextField()),
            ],
        ),
    ]