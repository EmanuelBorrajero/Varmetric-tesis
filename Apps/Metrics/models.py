import uuid
from django.db import models

# Etiqueta de los Intervalos de la Escala
class ScaleLabel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre",max_length=128)

    def __str__(self):
        self.name

    class Meta:
        db_table = 'ScaleLabel'
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'

# Rango de los Intervalos
class Range(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    min_value = models.FloatField(verbose_name="Desde")
    max_value = models.FloatField(verbose_name="Hasta")

    def __str__(self):
        return f"{self.min_value} - {self.max_value}"

    class Meta:
        db_table = 'Range'
        verbose_name = 'Rango'
        verbose_name_plural = 'Rangos'

# Intervalos de la Escala
class Interval(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    rangue = models.ManyToManyField(Range)
    scaleLabel = models.ManyToManyField(ScaleLabel)

    def __str__(self):
        return f"{self.interval} significa {self.scaleLabel}"

    class Meta:
        db_table = 'Interval'
        verbose_name = 'Intervalo'
        verbose_name_plural = 'Intervalos'

# Escala
class Scale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre",max_length=128)
    interval = models.ManyToManyField(Interval)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Scale'
        verbose_name = 'Escala'
        verbose_name_plural = 'Escalas'

# Variable
class Variable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=80)
    description = models.TextField("Descripción")
    scale = models.ManyToManyField(Scale)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Variable'
        verbose_name = 'Variable'
        verbose_name_plural = 'Variables'

# Dimensión
class Dimension(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    description = models.TextField("Descripción")
    weigh = models.IntegerField("Peso", default=0)
    variables = models.ManyToManyField(Variable)

    def __str__(self):
        return f"Dimension: {self.description} ({self.weigh})"

    class Meta:
        db_table = 'Dimension'
        verbose_name = 'Dimensión'
        verbose_name_plural = 'Dimensiones'

# Indicador
class Indicator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    description = models.TextField("Descripción")
    weigh = models.IntegerField("Peso", default=0)
    dimensions = models.ManyToManyField(Dimension)
    
    def __str__(self):
        return f"Indicador: {self.description} ({self.weigh})"

    class Meta:
        db_table = 'Indicator'
        verbose_name = 'Indicador'
        verbose_name_plural = 'Indicadores'

# Criterio de Medida
class MeasurementCriterion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    description = models.TextField("Descripción")
    max_value = models.IntegerField("Valor Máximo")
    value = models.IntegerField("Valor Obtenido",default=0)
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"Criterio de Medida: {self.description} valor máximo:{self.max_value}"

    class Meta:
        db_table = 'MeasurementCriterion'
        verbose_name = 'Criterio de Medida'
        verbose_name_plural = 'Criterios de Medida'