from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('seleccion/', login_required(Instruments.as_view()), name='select_instrument'),

    #Poll
    path('listado/encuesta/', login_required(PollList.as_view()), name='poll_list'),
    path('crear/encuesta/', login_required(PollCreate.as_view()), name='poll_create'),
    path('editar/encuesta/<pk>', login_required(PollUpdate.as_view()), name='poll_update'),
    path('eliminar/encuesta/<pk>', login_required(PollDelete.as_view()), name='poll_delete'),

    #Interview
    path('listado/entrevista/', login_required(InterviewList.as_view()), name='interview_list'),
    path('crear/entrevista/', login_required(InterviewCreate.as_view()), name='interview_create'),
    path('editar/entrevista/<pk>', login_required(InterviewUpdate.as_view()), name='interview_update'),
    path('eliminar/entrevista/<pk>', login_required(InterviewDelete.as_view()), name='interview_delete'),

    #Observation
    path('listado/observacion/', login_required(ObservationList.as_view()), name='observation_list'),
    path('crear/observacion/', login_required(ObservationCreate.as_view()), name='observation_create'),
    path('editar/observacion/<pk>', login_required(ObservationUpdate.as_view()), name='observation_update'),
    path('eliminar/observacion/<pk>', login_required(ObservationDelete.as_view()), name='observation_delete'),

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
    path('listado/criteriodeobservacion/observacion/<pk>', login_required(ObservationCriterionsList.as_view()), name='observation_criterions_list'),
    path('crear/criteriodeobservacion/observacion/<pk>', login_required(ObservationCriterionsCreate.as_view()), name='observation_criterions_create'),
    path('editar/criteriodeobservacion/observacion/<pk>', login_required(ObservationCriterionsUpdate.as_view()), name='observation_criterions_update'),
    path('eliminar/criteriodeobservacion/observacion/<pk>', login_required(ObservationCriterionsDelete.as_view()), name='observation_criterions_delete'),

    #REVIEW
    path('revicion/', login_required(ReviewInstruments.as_view()), name='review_instrument'),
    #Poll
    path('revicion/encuesta/lista', ReviewPollList.as_view(), name='poll_review_list'),
    path('revision/respuestas/encuesta/<pk>', ReviewAnswersPoll.as_view(), name='poll_review_answer'),
    path('revision/respuestas/encuesta/<uuid:poll_id>/usuario/<uuid:user_id>',ReviewAnswersPollUser.as_view(), name='poll_review_answer_user'),
    path('revision/respuestas/encuesta/resultado/<uuid:answer_id>/usuario/<uuid:user_id>',GetResultPoll.as_view(), name='get_result_poll'),
    path('revicion/encuesta/<pk>', ReviewPoll.as_view(), name='poll_review'),
    #Interview
    path('revicion/entrevista/lista', ReviewInterviewList.as_view(), name='interview_review_list'),
    path('revision/respuestas/entrevista/<pk>', ReviewAnswersInterview.as_view(), name='interview_review_answer'),
    path('revision/respuestas/entrevista/<uuid:interview_id>/usuario/<uuid:user_id>',ReviewAnswersInterviewUser.as_view(), name='interview_review_answer_user'),
    path('revision/respuestas/entrevista/resultado/<uuid:answer_id>/usuario/<uuid:user_id>',GetResultInterview.as_view(), name='get_result_interview'),
    path('revicion/entrevista/<pk>', ReviewInterview.as_view(), name='interview_review'),
    #Observation
    path('revicion/observacion/lista', ReviewObservationList.as_view(), name='observation_review_list'),
    path('revision/respuestas/observacion/<pk>', ReviewObservation.as_view(), name='observation_review_answer'),
    path('revision/respuestas/observacion/<uuid:observation_id>/usuario/<uuid:user_id>',ReviewObservationUser.as_view(), name='observation_review_answer_user'),
    path('revision/respuestas/observacion/resultado/<uuid:answer_id>/usuario/<uuid:user_id>',GetResultObservation.as_view(), name='get_result_observation'),

]