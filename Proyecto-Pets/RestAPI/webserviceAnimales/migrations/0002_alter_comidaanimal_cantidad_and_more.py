# Generated by Django 5.2 on 2025-05-19 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webserviceAnimales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comidaanimal',
            name='cantidad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='comidaanimal',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
