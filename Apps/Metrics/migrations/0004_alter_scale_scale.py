# Generated by Django 4.1.7 on 2023-11-28 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Metrics', '0003_remove_variable_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scale',
            name='scale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Metrics.variable'),
        ),
    ]
