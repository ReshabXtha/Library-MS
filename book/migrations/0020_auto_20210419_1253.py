# Generated by Django 3.2 on 2021-04-19 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0019_auto_20200224_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='IssuedDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 12, 53, 38, 842910)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='ReturnDate',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 26, 12, 53, 38, 842910)),
        ),
    ]
