import uuid
from ..AccesControl.models import User
from django.db import models

# Variable
class Variable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=200, unique=True)
    description = models.TextField("Descripción")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Variable'
        verbose_name = 'Variable'
        verbose_name_plural = 'Variables'

# Escala
class Scale(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    scale_label = models.CharField("Etiqueta", max_length=200, blank=True, null=True, unique=True)
    initial_value = models.FloatField("Valor Inicial")
    final_value = models.FloatField("Valor Final")
    scale = models.OneToOneField(Variable, on_delete=models.CASCADE)

    def __str__(self):
        return self.scale_label

    class Meta:
        db_table = 'Scale'
        verbose_name = 'Escala'
        verbose_name_plural = 'Escalas'

# Dimensión
class Dimension(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=200, unique=True)
    description = models.TextField("Descripción")
    weigh = models.FloatField("Peso", default=0)
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE)

    def __str__(self):
        return f"Dimension: {self.description} ({self.weigh})"

    class Meta:
        db_table = 'Dimension'
        verbose_name = 'Dimensión'
        verbose_name_plural = 'Dimensiones'

# Indicador
class Indicator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=200, unique=True)
    description = models.TextField("Descripción")
    weigh = models.FloatField("Peso", default=0)
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Indicador: {self.description} ({self.weigh})"

    class Meta:
        db_table = 'Indicator'
        verbose_name = 'Indicador'
        verbose_name_plural = 'Indicadores'

# Criterio de Medida
class MeasurementCriterion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=200, unique=True)
    description = models.TextField("Descripción")
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE, null=True)
    min_value = models.FloatField()
    max_value = models.FloatField()
    
    
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'MeasurementCriterion'
        verbose_name = 'Criterio de Medida'
        verbose_name_plural = 'Criterios de Medida'