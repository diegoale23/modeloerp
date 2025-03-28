# Generated by Django 5.1.7 on 2025-03-14 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('idReporte', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('financiero', 'Financiero'), ('inventario', 'Inventario'), ('pedidos', 'Pedidos')], max_length=50)),
                ('fecha_generacion', models.DateTimeField(auto_now_add=True)),
                ('parametros', models.JSONField()),
                ('contenido', models.TextField()),
            ],
        ),
    ]
