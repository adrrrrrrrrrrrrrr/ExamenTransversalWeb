# Generated by Django 5.0.3 on 2024-05-29 19:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('idModelo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'adrian_modelo',
            },
        ),
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('idAvion', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad_de_asientos', models.IntegerField()),
                ('modelo', models.ForeignKey(db_column='id_modelo', on_delete=django.db.models.deletion.CASCADE, to='venta.modelo')),
            ],
            options={
                'db_table': 'adrian_avion',
            },
        ),
    ]