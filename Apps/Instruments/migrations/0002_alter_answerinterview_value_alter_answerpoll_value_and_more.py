# Generated by Django 4.1.7 on 2023-06-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instruments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerinterview',
            name='value',
            field=models.FloatField(default=0, verbose_name='Valor Obtenido'),
        ),
        migrations.AlterField(
            model_name='answerpoll',
            name='value',
            field=models.FloatField(default=0, verbose_name='Valor Obtenido'),
        ),
        migrations.AlterField(
            model_name='observationresult',
            name='value',
            field=models.FloatField(default=0, verbose_name='Valor Obtenido'),
        ),
    ]
