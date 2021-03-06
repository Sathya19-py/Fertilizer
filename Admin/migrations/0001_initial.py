# Generated by Django 3.1.1 on 2020-09-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Govt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('House_Number', models.CharField(max_length=50)),
                ('Village_Name', models.CharField(max_length=50)),
                ('Mandal_Name', models.CharField(max_length=50)),
                ('District_Name', models.CharField(max_length=50)),
                ('State_Name', models.CharField(max_length=50)),
                ('Aadhaar_Number', models.IntegerField()),
                ('PassBook_Number', models.CharField(max_length=20)),
                ('Land', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
