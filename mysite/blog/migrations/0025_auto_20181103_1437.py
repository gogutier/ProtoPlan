# Generated by Django 2.0.5 on 2018-11-03 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20181102_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diaconv',
            name='diaajust',
            field=models.DateField(default=datetime.datetime(2018, 11, 3, 0, 0)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2018, 11, 3, 14, 37, 24, 458643)),
        ),
    ]