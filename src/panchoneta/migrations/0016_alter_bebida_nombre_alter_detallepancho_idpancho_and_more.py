# Generated by Django 5.2.3 on 2025-06-25 23:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panchoneta', '0015_alter_detallebebidaventa_cantidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebida',
            name='nombre',
            field=models.CharField(blank=True, help_text='nombre de la bebida', max_length=120, null=True, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='detallepancho',
            name='idPancho',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='panchoneta.pancho', verbose_name='Pancho'),
        ),
        migrations.AlterField(
            model_name='detallepancho',
            name='idSalsa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='panchoneta.salsa', verbose_name='Salsa'),
        ),
        migrations.AlterField(
            model_name='pancho',
            name='nombre',
            field=models.CharField(help_text='nombre del pancho', max_length=120, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='salsa',
            name='nombre',
            field=models.CharField(blank=True, help_text='nombre de la salsa', max_length=120, null=True, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='calle',
            field=models.CharField(blank=True, help_text='calle de la sucursal', max_length=120, null=True, verbose_name='calle'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='nombre',
            field=models.CharField(blank=True, help_text='nombre de la sucursal', max_length=120, null=True, verbose_name='nombre'),
        ),
    ]
