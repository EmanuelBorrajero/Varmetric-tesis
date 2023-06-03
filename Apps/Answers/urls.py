from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    #urls AnswersPoll
    path('encuestas/', login_required(AnswersPollList.as_view()), name= 'answers_poll_list' ),

    #urls AnswersInterview
    path('entrevistas/', login_required(AnswersInterviewList.as_view()), name= 'answers_interview_list' ),

    #urls AnswersObservation
    path('obserbacion/', login_required(AnswersObservationList.as_view()), name= 'answers_obervation_list' ),
]
