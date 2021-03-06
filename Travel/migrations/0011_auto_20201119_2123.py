# Generated by Django 3.1.3 on 2020-11-19 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0010_auto_20201119_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='cab',
            name='air_conditioned',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cab',
            name='car_photo',
            field=models.ImageField(default=None, null=True, upload_to='uploads/cab_cars'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 19, 21, 23, 59, 184103)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 19, 21, 23, 59, 184026)),
        ),
    ]
