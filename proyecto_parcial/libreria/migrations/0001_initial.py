# Generated by Django 3.2.8 on 2023-05-13 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('NombreProducto', models.CharField(max_length=100)),
                ('Marca', models.CharField(max_length=100)),
                ('Unidades', models.IntegerField(null=True)),
                ('Compra', models.FloatField(null=True)),
                ('Venta', models.FloatField(null=True)),
            ],
        ),
    ]
