import uuid
from django.db import models
from django.contrib.auth import get_user_model
from Metrics.models import MeasurementCriterion
User = get_user_model() 

class Answer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    answer = models.TextField("Respuesta", max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Respuesta'
        verbose_name = 'Respuesta'
        verbose_name_plural = 'Respuestas'

class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    text = models.CharField("Nombre", max_length=80)
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    measurementCriterions = models.ManyToManyField(MeasurementCriterion)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Encuesta'
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuesta'

class Poll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=80)
    description = models.TextField("Descripción")
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Encuesta'
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuesta'

class Interview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=80)
    description = models.TextField("Descripción")
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Entrevista'
        verbose_name = 'Entrevista'
        verbose_name_plural = 'Entrevistas'

class Observation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=80)
    description = models.TextField("Descripción")
    observationCriterions = models.ManyToManyField(MeasurementCriterion)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Observación'
        verbose_name = 'Observación'
        verbose_name_plural = 'Observaciones'

