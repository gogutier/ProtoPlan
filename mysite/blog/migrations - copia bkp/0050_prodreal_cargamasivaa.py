# Generated by Django 2.0.5 on 2018-10-13 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0049_remove_prodreal_cargamasivaa'),
    ]

    operations = [
        migrations.AddField(
            model_name='prodreal',
            name='cargamasivaa',
            field=models.ForeignKey(default='vacio', on_delete=django.db.models.deletion.CASCADE, related_name='fecha_carga_producciones', to='blog.CargaProducciones'),
        ),
    ]
