# Generated by Django 4.2 on 2023-04-23 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='apartment_number',
            field=models.IntegerField(default=0, verbose_name='ApartmentNumber'),
        ),
    ]