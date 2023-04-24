# Generated by Django 4.2 on 2023-04-24 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0005_tenant_apartment_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='email',
            field=models.CharField(default='', max_length=240, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='lease_start',
            field=models.DateField(null=True, verbose_name='Lease Start'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='phone_number',
            field=models.CharField(default='', max_length=20, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='apartment_number',
            field=models.IntegerField(default=0, verbose_name='Apartment Number'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='first_name',
            field=models.CharField(default='', max_length=240, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='last_name',
            field=models.CharField(default='', max_length=240, verbose_name='Last Name'),
        ),
    ]