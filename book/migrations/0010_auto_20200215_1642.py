# Generated by Django 2.2.5 on 2020-02-15 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_auto_20200126_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='IssuedDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 15, 16, 42, 50, 577974)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='ReturnDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 16, 42, 50, 577974)),
        ),
    ]
