from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    #urls AnswersPoll
    path('encuestas/', login_required(AnswersPollList.as_view()), name= 'answers_poll_list' ),
    path('encuestas/responder/<pk>', login_required(AnswerPollReply.as_view()), name= 'answers_poll_replay' ),

    #urls AnswersInterview
    path('entrevistas/', login_required(AnswersInterviewList.as_view()), name= 'answers_interview_list' ),
    path('entrevistas/responder/<pk>', login_required(AnswerInterviewReply.as_view()), name= 'answers_interview_replay' ),

    #urls AnswersObservation
    path('observacion/', login_required(AnswersObservationList.as_view()), name= 'answers_obervation_list' ),
    path('observacion/responder/<pk>', login_required(AnswerObservationReply.as_view()), name= 'answers_observation_replay' ),
]
