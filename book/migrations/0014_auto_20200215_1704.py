# Generated by Django 2.2.5 on 2020-02-15 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0013_auto_20200215_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='IssuedDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 15, 17, 4, 29, 279852)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='ReturnDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 22, 17, 4, 29, 279852)),
        ),
    ]
