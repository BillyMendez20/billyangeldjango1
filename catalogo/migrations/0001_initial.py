# Generated by Django 4.1.7 on 2023-03-18 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cantidad', models.IntegerField()),
                ('cantidad_vendida', models.IntegerField(default=0)),
                ('cantidad_disponible', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.categoria')),
            ],
        ),
    ]