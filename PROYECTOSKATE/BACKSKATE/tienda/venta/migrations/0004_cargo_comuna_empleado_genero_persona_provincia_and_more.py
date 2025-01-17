# Generated by Django 5.0.3 on 2024-05-30 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0003_rename_idmodelo_modelo_id_modelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('idCargo', models.IntegerField(db_column='codCargo', primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'adrian_cargo',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.IntegerField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'adrian_comuna',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.AutoField(primary_key=True, serialize=False)),
                ('sueldo', models.IntegerField()),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
                ('codCargo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='venta.cargo')),
            ],
            options={
                'db_table': 'adrian_empleado',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('idGenero', models.AutoField(db_column='id_genero', primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(db_column='genero', max_length=20)),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'adrian_genero',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('rut', models.IntegerField(primary_key=True, serialize=False)),
                ('dv', models.CharField(max_length=1)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('papellido', models.CharField(blank=True, max_length=30, null=True)),
                ('sapellido', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('fechaNacimiento', models.DateField(auto_now_add=True, db_column='fecha_nacimiento', null=True)),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
                ('activo', models.IntegerField(blank=True, null=True)),
                ('comuna', models.ForeignKey(db_column='id_comuna', on_delete=django.db.models.deletion.DO_NOTHING, to='venta.comuna')),
                ('genero', models.ForeignKey(db_column='id_genero', on_delete=django.db.models.deletion.DO_NOTHING, to='venta.genero')),
            ],
            options={
                'db_table': 'adrian_persona',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('idProvincia', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'adrian_provincia',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fCreacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'adrian_region',
            },
        ),
        migrations.DeleteModel(
            name='Vendedor',
        ),
        migrations.AddField(
            model_name='empleado',
            name='rut',
            field=models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.DO_NOTHING, to='venta.persona'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='provincia',
            field=models.ForeignKey(db_column='id_provincia', on_delete=django.db.models.deletion.CASCADE, to='venta.provincia'),
        ),
        migrations.AddField(
            model_name='provincia',
            name='region',
            field=models.ForeignKey(db_column='id_region', on_delete=django.db.models.deletion.CASCADE, to='venta.region'),
        ),
    ]
