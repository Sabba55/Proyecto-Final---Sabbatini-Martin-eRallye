# Generated by Django 4.1.5 on 2023-02-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('nacionalidad', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
                ('inscriptos', models.IntegerField()),
                ('kilometraje', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Copiloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.IntegerField(default=15)),
                ('nacionalidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.IntegerField(default=17)),
                ('nacionalidad', models.CharField(max_length=20)),
                ('marca_vehiculo', models.CharField(max_length=40)),
                ('modelo_vehiculo', models.CharField(max_length=40)),
            ],
        ),
    ]
