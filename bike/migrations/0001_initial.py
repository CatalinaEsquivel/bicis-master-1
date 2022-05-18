# Generated by Django 4.0.4 on 2022-05-11 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('idServicio', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreServicio', models.CharField(max_length=50, verbose_name='Nombre Servicio')),
                ('descripcionServicio', models.CharField(blank=True, max_length=20, null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='tipoServicio',
            fields=[
                ('idTipoServicio', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Patente')),
                ('nombreTipoServicio', models.CharField(max_length=20, verbose_name='Marca')),
                ('descripcionTipoServicio', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bike.servicio')),
            ],
        ),
    ]