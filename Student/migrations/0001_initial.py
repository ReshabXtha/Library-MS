# Generated by Django 2.2.5 on 2019-12-14 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('StudentName', models.CharField(max_length=100)),
                ('StudentAddress', models.CharField(max_length=100)),
                ('StudentFaculty', models.CharField(choices=[('BCA', 'BCA'), ('Bsc.CSIT', 'Bsc.CSIT')], max_length=10)),
                ('StudentContact', models.CharField(default='', max_length=50)),
                ('StudentEmail', models.CharField(default='', max_length=100)),
                ('StudentProfile', models.ImageField(blank=True, null=True, upload_to='Media')),
            ],
        ),
    ]