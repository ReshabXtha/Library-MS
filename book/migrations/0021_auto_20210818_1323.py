# Generated by Django 3.2 on 2021-08-18 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0020_auto_20210419_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='IssuedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 18, 13, 23, 47, 371624)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='ReturnDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 25, 13, 23, 47, 371624)),
        ),
    ]
