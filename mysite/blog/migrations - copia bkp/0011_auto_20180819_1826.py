# Generated by Django 2.0.5 on 2018-08-19 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180819_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='AppointmentType',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Clinician',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Duration',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Patient',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='Time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
