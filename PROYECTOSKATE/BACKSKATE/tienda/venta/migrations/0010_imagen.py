# Generated by Django 5.0.3 on 2024-06-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0009_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('archivo', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
