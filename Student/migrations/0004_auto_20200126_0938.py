# Generated by Django 2.2.5 on 2020-01-26 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_auto_20200126_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='StudentFaculty',
            field=models.CharField(choices=[('BCA', 'BCA'), ('Bsc.CSIT', 'Bsc.CSIT')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='StudentSemester',
            field=models.CharField(choices=[('1st Sem', '1st Sem'), ('2st Sem', '2st Sem'), ('3st Sem', '3st Sem'), ('4st Sem', '4st Sem'), ('5st Sem', '5st Sem'), ('6st Sem', '6st Sem'), ('7st Sem', '7st Sem'), ('8st Sem', '8st Sem')], max_length=50),
        ),
    ]
