import uuid
from django.db import models
from ..AccesControl.models import User
from ..Metrics.models import MeasurementCriterion


class Poll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=80, unique=True)
    description = models.TextField("Descripción")
    anonymous = models.BooleanField("Anónimo", default=False)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Encuesta'
        verbose_name = 'Encuesta'
        verbose_name_plural = 'Encuesta'


class Interview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=80, unique=True)
    description = models.TextField("Descripción")
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Entrevista'
        verbose_name = 'Entrevista'
        verbose_name_plural = 'Entrevistas'


class Observation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=80, unique=True)
    description = models.TextField("Descripción")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Observación'
        verbose_name = 'Observación'
        verbose_name_plural = 'Observaciones'


class QuestionPoll(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=80, unique=True)
    text = models.TextField("Texto de la pregunta")
    measurementCriterions = models.OneToOneField(MeasurementCriterion, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'PreguntaEncuesta'
        verbose_name = 'Pregunta de la Encuesta'
        verbose_name_plural = 'Preguntas de la Encuesta'


class QuestionInterview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField("Nombre", max_length=80, unique=True)
    text = models.TextField("Texto de la pregunta")
    measurementCriterions = models.OneToOneField(MeasurementCriterion, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'PreguntaEntrevista'
        verbose_name = 'Pregunta de la Entrevista'
        verbose_name_plural = 'Preguntas de la Entrevista'


class AnswerPoll(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    answer = models.TextField("Respuesta", max_length=255)
    value = models.FloatField("Valor Obtenido", default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questionPoll = models.ForeignKey(QuestionPoll, on_delete=models.CASCADE)
    

    class Meta:
        db_table = 'RespuestaEncuesta'
        verbose_name = 'Respuesta Encuesta'
        verbose_name_plural = 'Respuestas Encuesta'


class AnswerInterview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    answer = models.TextField("Respuesta", max_length=255)
    value = models.FloatField("Valor Obtenido", default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    questionInterview = models.ForeignKey(QuestionInterview, on_delete=models.CASCADE)

    class Meta:
        db_table = 'RespuestaEntrevista'
        verbose_name = 'Respuesta Entrevista'
        verbose_name_plural = 'Respuestas Entrevista'


class ObservationCriterions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    criterion = models.TextField("Criterio", max_length=255, unique=True)
    measurementCriterions = models.OneToOneField(MeasurementCriterion, on_delete=models.CASCADE)
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)

    class Meta:
        db_table = 'CriterioObservacion'
        verbose_name = 'Criterio de Observacion'
        verbose_name_plural = 'Criterios de Observacion'


class ObservationResult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    value = models.FloatField(verbose_name="Valor Obtenido", default=0, null=True, blank=True)
    observationCriterions = models.ForeignKey(ObservationCriterions, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ResultadoObservacion'
        verbose_name = 'Resultado de la Observacion'
        verbose_name_plural = 'Resultados de las Observaciones'
