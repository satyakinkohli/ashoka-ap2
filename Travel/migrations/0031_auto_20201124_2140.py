# Generated by Django 3.1.1 on 2020-11-24 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0030_auto_20201124_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 24, 21, 40, 3, 535074)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 24, 21, 40, 3, 535074)),
        ),
    ]
