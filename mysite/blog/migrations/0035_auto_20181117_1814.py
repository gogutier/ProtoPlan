# Generated by Django 2.0.5 on 2018-11-17 21:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20181117_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(default='vacio', max_length=10, unique=True)),
                ('mescorto', models.CharField(default='vacio', max_length=10, unique=True)),
                ('mesnum', models.CharField(default='vacio', max_length=10, unique=True)),
                ('dias', models.CharField(default='vacio', max_length=10, unique=True)),
                ('diasnoprod', models.CharField(default='vacio', max_length=10, unique=True)),
                ('año', models.CharField(default='vacio', max_length=10, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='minuta',
            name='dia',
            field=models.DateField(default=datetime.datetime(2018, 11, 17, 18, 14, 2, 405132)),
        ),
        migrations.AlterField(
            model_name='minuta',
            name='texto',
            field=models.TextField(default='.'),
        ),
    ]