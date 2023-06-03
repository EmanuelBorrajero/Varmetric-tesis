from django.views.generic import ListView 
from ..Instruments.models import *

#AnswersPoll
class AnswersPollList(ListView):
    model = Poll
    template_name = 'Answers/answer_poll_list.html'

#AnswersInterview
class AnswersInterviewList(ListView):
    model = Interview
    template_name = 'Answers/answer_interview_list.html'

#AnswersObservation
class AnswersObservationList(ListView):
    model = Observation
    template_name = 'Answers/answer_observation_list.html'
