from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    #Poll
    path('seleccion/', login_required(Instruments.as_view()), name='select_instrument'),
    path('listado/encuesta/', login_required(PollList.as_view()), name='poll_list'),
    path('crear/encuesta/', login_required(PollCreate.as_view()), name='poll_create'),
    path('editar/encuesta/<pk>', login_required(PollUpdate.as_view()), name='poll_update'),
    path('eliminar/encuesta/<pk>', login_required(PollDelete.as_view()), name='poll_delete'),
    path('detalles/encuesta/<pk>', login_required(PollDetail.as_view()), name='poll_detail'),

    #Interview
    path('listado/entrevista/', login_required(InterviewList.as_view()), name='interview_list'),
    path('crear/entrevista/', login_required(InterviewCreate.as_view()), name='interview_create'),
    path('editar/entrevista/<pk>', login_required(InterviewUpdate.as_view()), name='interview_update'),
    path('eliminar/entrevista/<pk>', login_required(InterviewDelete.as_view()), name='interview_delete'),
    path('detalles/entrevista/<pk>', login_required(InterviewDetail.as_view()), name='interview_detail'),

    #Observation
    path('listado/observacion/', login_required(ObservationList.as_view()), name='observation_list'),
    path('crear/observacion/', login_required(ObservationCreate.as_view()), name='observation_create'),
    path('editar/observacion/<pk>', login_required(ObservationUpdate.as_view()), name='observation_update'),
    path('eliminar/observacion/<pk>', login_required(ObservationDelete.as_view()), name='observation_delete'),
    path('detalles/observacion/<pk>', login_required(ObservationDetail.as_view()), name='observation_detail'),

    #QuentionPoll
    path('listado/pregunta/encuesta/<pk>', login_required(QuestionPollList.as_view()), name='question_poll_list'),
    path('crear/pregunta/encuesta/<pk>', login_required(QuestionPollCreate.as_view()), name='question_poll_create'),
    path('editar/pregunta/encuesta/<pk>', login_required(QuestionPollUpdate.as_view()), name='question_poll_update'),
    path('eliminar/pregunta/encuesta/<pk>', login_required(QuestionPollDelete.as_view()), name='question_poll_delete'),

    #QuestionInterview
    path('listado/pregunta/entrevista/<pk>', login_required(QuestionInterviewList.as_view()), name='question_interview_list'),
    path('crear/pregunta/entrevista/<pk>', login_required(QuestionInterviewCreate.as_view()), name='question_interview_create'),
    path('editar/pregunta/entrevista/<pk>', login_required(QuestionInterviewUpdate.as_view()), name='question_interview_update'),
    path('eliminar/pregunta/entrevista/<pk>', login_required(QuestionInterviewDelete.as_view()), name='question_interview_delete'),

    #ObservationCriterions
    path('listado/criterio de observacion/observacion/<pk>', login_required(ObservationCriterionsList.as_view()), name='observation_criterions_list'),
    path('crear/criterio de observacion/observacion/<pk>', login_required(ObservationCriterionsCreate.as_view()), name='observation_criterions_create'),
    path('editar/criterio de observacion/observacion/<pk>', login_required(ObservationCriterionsUpdate.as_view()), name='observation_criterions_update'),
    path('eliminar/criterio de observacion/observacion/<pk>', login_required(ObservationCriterionsDelete.as_view()), name='observation_criterions_delete'),
]