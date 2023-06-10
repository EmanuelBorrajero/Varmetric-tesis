from django.shortcuts import render, redirect
from django.views.generic import View, ListView 
from django.shortcuts import get_object_or_404
from ..AccesControl.models import User
from ..Instruments.models import *
from .forms import AnswerObservationReplyForm
#AnswersPoll
class AnswersPollList(ListView):
    model = Poll
    template_name = 'Answers/answer_poll_list.html'

class AnswerPollReply(View):
    moldel = QuestionPoll
    template_name = 'Answers/answer_poll_reply.html'

    def get_queryset(self):
        poll = get_object_or_404(
                    Poll,
                    id = self.kwargs['pk']
                )
        return poll

    def get_context_data(self, **kwargs):
        context = {}
        context["poll"] = self.get_queryset()
        context["question_poll"] = self.moldel.objects.filter(poll = self.get_queryset())
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self,request,*args,**kwargs):
        questionPoll = self.moldel.objects.filter(poll = self.get_queryset())
        for question in questionPoll:
            AnswerPoll.objects.create(
                answer = request.POST[str(question.name)],
                user = get_object_or_404(
                            User,
                            id = request.POST['user']
                        ),
                questionPoll = question,
            )
        return redirect('Answers:answers_poll_list')

#AnswersInterview
class AnswersInterviewList(ListView):
    model = Interview
    template_name = 'Answers/answer_interview_list.html'

class AnswerInterviewReply(View):
    moldel = QuestionInterview
    template_name = 'Answers/answer_interview_reply.html'

    def get_queryset(self):
        interview = get_object_or_404(
                    Interview,
                    id = self.kwargs['pk']
                )
        return interview

    def get_context_data(self, **kwargs):
        context = {}
        context["interview"] = self.get_queryset()
        context["question_interview"] = self.moldel.objects.filter(interview = self.get_queryset())
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self,request,*args,**kwargs):
        questionInterview = self.moldel.objects.filter(interview = self.get_queryset())
        for question in questionInterview:
            AnswerInterview.objects.create(
                answer = request.POST[str(question.name)],
                user = get_object_or_404(
                            User,
                            id = request.POST['user']
                        ),
                questionInterview = question,
            )
        return redirect('Answers:answers_interview_list')

#AnswersObservation
class AnswersObservationList(ListView):
    model = Observation
    template_name = 'Answers/answer_observation_list.html'

class AnswerObservationReply(View):
    moldel = ObservationCriterions
    template_name = 'Answers/answer_observation_reply.html'
    form_class = AnswerObservationReplyForm

    def get_queryset(self):
        observation = get_object_or_404(
                    Observation,
                    id = self.kwargs['pk']
                )
        return observation

    def get_context_data(self, **kwargs):
        context = {}
        context["observation"] = self.get_queryset()
        context["observation_criterions"] = self.moldel.objects.filter(observation = self.get_queryset())
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self,request,*args,**kwargs):
        observationCriterions = self.moldel.objects.filter(observation = self.get_queryset())
        for observationCriterion in observationCriterions:
            ObservationResult.objects.create(
                value = request.POST[str(observationCriterion.criterion)],
                user = get_object_or_404(
                            User,
                            id = request.POST['user']
                        ),
                observationCriterions = observationCriterion,
            )
        return redirect('Answers:answers_obervation_list')