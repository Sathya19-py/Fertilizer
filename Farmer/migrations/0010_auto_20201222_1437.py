# Generated by Django 3.0.6 on 2020-12-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0009_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Order_Id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='Land',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
