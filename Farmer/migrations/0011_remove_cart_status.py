# Generated by Django 3.0.6 on 2020-12-22 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0010_auto_20201222_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='Status',
        ),
    ]