# Generated by Django 3.0.6 on 2020-07-30 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Farmer', '0002_auto_20200730_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Index_Id', models.IntegerField()),
                ('Email', models.EmailField(default=0, max_length=100)),
                ('Order_Id', models.IntegerField(default=0, unique=True)),
                ('Order_Status', models.CharField(default=0, max_length=100)),
                ('Quantity', models.IntegerField()),
                ('Payment_Mode', models.CharField(default=0, max_length=100)),
                ('Payment_Status', models.CharField(default=0, max_length=100)),
                ('Delivery_Address', models.TextField()),
                ('Time', models.TimeField(auto_now=True)),
                ('Date', models.DateField(auto_now=True)),
            ],
        ),
    ]