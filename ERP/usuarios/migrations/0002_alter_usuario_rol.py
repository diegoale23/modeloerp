# Generated by Django 5.1.7 on 2025-03-17 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('administrador', 'Administrador'), ('empleado', 'Empleado'), ('cliente', 'Cliente')], default='cliente', max_length=20),
        ),
    ]
