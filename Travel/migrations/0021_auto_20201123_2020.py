# Generated by Django 3.1.1 on 2020-11-23 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travel', '0020_merge_20201123_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.CharField(blank=True, default='The most comfortable stay', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='flight',
            name='arrival_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 23, 20, 20, 19, 881811)),
        ),
        migrations.AlterField(
            model_name='flight',
            name='departure_time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 23, 20, 20, 19, 881811)),
        ),
    ]
