# Generated by Django 2.2.5 on 2019-12-22 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20191222_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbook',
            name='IssuedTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.Student'),
        ),
    ]
