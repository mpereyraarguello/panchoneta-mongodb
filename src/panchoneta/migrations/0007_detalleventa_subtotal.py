# Generated by Django 5.2.3 on 2025-06-24 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panchoneta', '0006_remove_detalleventa_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalleventa',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, verbose_name='subtotal'),
        ),
    ]
