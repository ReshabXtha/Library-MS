# Generated by Django 2.2.5 on 2020-02-24 04:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0018_auto_20200215_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='IssuedDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 24, 10, 15, 51, 478052)),
        ),
        migrations.AlterField(
            model_name='issuedbook',
            name='ReturnDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 2, 10, 15, 51, 478052)),
        ),
    ]
