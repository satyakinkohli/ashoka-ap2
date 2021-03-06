# Generated by Django 3.1.3 on 2020-11-19 21:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0011_auto_20201119_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='car_options',
            name='type_options',
            field=models.ImageField(default=None, null=True, upload_to='uploads/cab_types'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 19, 21, 51, 20, 540252)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 19, 21, 51, 20, 540225)),
        ),
    ]
