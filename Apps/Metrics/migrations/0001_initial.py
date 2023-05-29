# Generated by Django 4.1.7 on 2023-05-29 16:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('weigh', models.FloatField(default=0, verbose_name='Peso')),
            ],
            options={
                'verbose_name': 'Dimensión',
                'verbose_name_plural': 'Dimensiones',
                'db_table': 'Dimension',
            },
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('weigh', models.FloatField(default=0, verbose_name='Peso')),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Metrics.dimension')),
            ],
            options={
                'verbose_name': 'Indicador',
                'verbose_name_plural': 'Indicadores',
                'db_table': 'Indicator',
            },
        ),
        migrations.CreateModel(
            name='Interval',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Intervalo',
                'verbose_name_plural': 'Intervalos',
                'db_table': 'Interval',
            },
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('min_value', models.FloatField(verbose_name='Desde')),
                ('max_value', models.FloatField(verbose_name='Hasta')),
            ],
            options={
                'verbose_name': 'Rango',
                'verbose_name_plural': 'Rangos',
                'db_table': 'Range',
            },
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('interval', models.ManyToManyField(to='Metrics.interval')),
            ],
            options={
                'verbose_name': 'Escala',
                'verbose_name_plural': 'Escalas',
                'db_table': 'Scale',
            },
        ),
        migrations.CreateModel(
            name='ScaleLabel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Etiqueta',
                'verbose_name_plural': 'Etiquetas',
                'db_table': 'ScaleLabel',
            },
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('scale', models.ManyToManyField(to='Metrics.scale')),
            ],
            options={
                'verbose_name': 'Variable',
                'verbose_name_plural': 'Variables',
                'db_table': 'Variable',
            },
        ),
        migrations.CreateModel(
            name='MeasurementCriterion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('value', models.IntegerField(default=0, verbose_name='Valor Obtenido')),
                ('indicator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Metrics.indicator')),
            ],
            options={
                'verbose_name': 'Criterio de Medida',
                'verbose_name_plural': 'Criterios de Medida',
                'db_table': 'MeasurementCriterion',
            },
        ),
        migrations.AddField(
            model_name='interval',
            name='rangue',
            field=models.ManyToManyField(to='Metrics.range'),
        ),
        migrations.AddField(
            model_name='interval',
            name='scaleLabel',
            field=models.ManyToManyField(to='Metrics.scalelabel'),
        ),
        migrations.AddField(
            model_name='dimension',
            name='variable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Metrics.variable'),
        ),
    ]