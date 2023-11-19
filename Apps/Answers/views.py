from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.generic import View, ListView

from .forms import AnswerObservationReplyForm
from ..Instruments.models import *


# AnswersPoll
class AnswersPollList(ListView):
    model = Poll
    template_name = 'Answers/answer_poll_list.html'

    def get_queryset(self):
        return Poll.objects.all().exclude(
            users=self.request.user
        )


class AnswerPollReply(View):
    moldel = QuestionPoll
    template_name = 'Answers/answer_poll_reply.html'

    def get_queryset(self):
        poll = get_object_or_404(
            Poll,
            id=self.kwargs['pk']
        )
        return poll

    def get_context_data(self, **kwargs):
        context = {}
        context["poll"] = self.get_queryset()
        context["question_poll"] = self.moldel.objects.order_by('name').filter(poll=self.get_queryset())
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        questionPoll = self.moldel.objects.filter(poll=self.get_queryset())
        for question in questionPoll:
            AnswerPoll.objects.create(
                answer=request.POST[str(question.name)],
                user=self.request.user,
                questionPoll=question,
            )
        poll = self.get_queryset()
        poll.users.add(self.request.user)
        poll.save()
        return redirect('Answers:answers_poll_list')


# AnswersInterview
class AnswersInterviewList(ListView):
    model = Interview
    template_name = 'Answers/answer_interview_list.html'
    
    def get_queryset(self):
        return Interview.objects.all().exclude(
            users=self.request.user
        )

class AnswerInterviewReply(View):
    moldel = QuestionInterview
    template_name = 'Answers/answer_interview_reply.html'

    def get_queryset(self):
        interview = get_object_or_404(
            Interview,
            id=self.kwargs['pk']
        )
        return interview

    def get_context_data(self, **kwargs):
        context = {}
        context["interview"] = self.get_queryset()
        context["question_interview"] = self.moldel.objects.order_by('name').filter(interview=self.get_queryset())
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        questionInterview = self.moldel.objects.filter(interview=self.get_queryset())
        for question in questionInterview:
            AnswerInterview.objects.create(
                answer=request.POST[str(question.name)],
                user=get_object_or_404(
                    User,
                    id=request.POST['user']
                ),
                questionInterview=question,
            )
        interview = self.get_queryset()
        interview.users.add(self.request.user)
        interview.save()
        return redirect('Answers:answers_interview_list')


# AnswersObservation
class AnswersObservationList(ListView):
    model = Observation
    template_name = 'Answers/answer_observation_list.html'

    def get_queryset(self):
        return Observation.objects.all()

class AnswerObservationReply(View):
    moldel = ObservationCriterions
    template_name = 'Answers/answer_observation_reply.html'
    form_class = AnswerObservationReplyForm

    def get_queryset(self):
        observation = get_object_or_404(
            Observation,
            id=self.kwargs.get('pk', None)
        )
        return observation

    def get_context_data(self, **kwargs):
        context = {}
        context["observation"] = self.get_queryset()
        context["observation_criterions"] = self.moldel.objects.order_by('criterion').filter(observation=self.get_queryset())
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        observationCriterions = self.moldel.objects.filter(observation=self.get_queryset())
        for observationCriterion in observationCriterions:
            ObservationResult.objects.create(
                value=request.POST[str(observationCriterion.criterion)],
                user=get_object_or_404(
                    User,
                    id=request.POST['user']
                ),
                observationCriterions=observationCriterion,
            )
        return redirect('Answers:answers_obervation_list')
