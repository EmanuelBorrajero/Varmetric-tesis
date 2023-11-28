from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from AprendizajeCreativo.mixins import IsStaffUserMixin
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from Apps.Metrics.calculation import *
from .models import *
from .forms import *


class Instruments(IsStaffUserMixin, TemplateView):
    template_name = "Instruments/instruments.html"


# Poll
class PollList(IsStaffUserMixin, ListView):
    model = Poll
    template_name = 'Instruments/poll_list.html'


class PollCreate(IsStaffUserMixin, CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'Instruments/poll_create.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                message = 'Encuesta creada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La encuesta no se ha podido crear!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:poll_list')


class PollUpdate(IsStaffUserMixin, UpdateView):
    model = Poll
    form_class = PollForm
    template_name = 'Instruments/poll_update.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = 'Encuesta modificada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La encuesta no se ha podido modificar!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:poll_list')


class PollDelete(IsStaffUserMixin, DeleteView):
    model = Poll
    template_name = 'Instruments/poll_delete.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            poll = self.get_object()
            poll.delete()
            message = 'Encuesta eliminada corréctamente!!'
            error = 'No hay Error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Instruments:poll_list')

# Interview
class InterviewList(IsStaffUserMixin, ListView):
    model = Interview
    template_name = 'Instruments/interview_list.html'


class InterviewCreate(IsStaffUserMixin, CreateView):
    model = Interview
    form_class = InterviewForm
    template_name = 'Instruments/interview_create.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                message = 'Entrevista creada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La entrevista no se ha podido crear!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:interview_list')


class InterviewUpdate(IsStaffUserMixin, UpdateView):
    model = Interview
    form_class = InterviewForm
    template_name = 'Instruments/interview_update.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = 'Entrevista modificada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La entrevista no se ha podido modificar!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:interview_list')


class InterviewDelete(IsStaffUserMixin, DeleteView):
    model = Interview
    template_name = 'Instruments/interview_delete.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            interview = self.get_object()
            interview.delete()
            message = 'Entrevista eliminada corréctamente!!'
            error = 'No hay Error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Instruments:interview_list')

# Observation
class ObservationList(IsStaffUserMixin, ListView):
    model = Observation
    template_name = 'Instruments/observation_list.html'


class ObservationCreate(IsStaffUserMixin, CreateView):
    model = Observation
    form_class = ObservationForm
    template_name = 'Instruments/observation_create.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                message = 'Observación creada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La observación no se ha podido crear!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:observation_list')


class ObservationUpdate(IsStaffUserMixin, UpdateView):
    model = Observation
    form_class = ObservationForm
    template_name = 'Instruments/observation_update.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = 'Observación modificada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La observación no se ha podido modificar!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:observation_list')


class ObservationDelete(IsStaffUserMixin, DeleteView):
    model = Observation
    template_name = 'Instruments/observation_delete.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            observation = self.get_object()
            observation.delete()
            message = 'Observación eliminada corréctamente!!'
            error = 'No hay Error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Instruments:observation_list')

# QuestionPoll
class QuestionPollList(IsStaffUserMixin, ListView):
    model = QuestionPoll
    template_name = 'Instruments/question_poll_list.html'

    def get_queryset(self):
        poll = Poll.objects.get(id=self.kwargs['pk'])
        queryset = self.model.objects.order_by('name').filter(poll=poll)
        return {'queryset': queryset, 'poll': poll}


class QuestionPollCreate(IsStaffUserMixin, CreateView):
    model = QuestionPoll
    form_class = QuestionPollForm
    template_name = 'Instruments/question_poll_create.html'

    def get_queryset(self):
        poll = get_object_or_404(
            Poll,
            id=self.kwargs['pk']
        )
        return poll

    def get_context_data(self, **kwargs):
        context = {}
        context["poll"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                poll = self.get_queryset()
                QuestionPoll.objects.create(
                    name=form.cleaned_data.get('name'),
                    text=form.cleaned_data.get('text'),
                    measurementCriterions=form.cleaned_data.get('measurementCriterions'),
                    poll=poll,
                )
                message = 'Pregunta creada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La pregunta no se ha podido crear!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:poll_list')


class QuestionPollUpdate(IsStaffUserMixin, UpdateView):
    model = QuestionPoll
    form_class = QuestionPollForm
    template_name = 'Instruments/question_poll_update.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = 'Pregunta modificada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La pregunta no se ha podido modificar!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:poll_list')


class QuestionPollDelete(IsStaffUserMixin, DeleteView):
    model = QuestionPoll
    template_name = 'Instruments/question_poll_delete.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            question = self.get_object()
            question.delete()
            message = 'Pregunta eliminada corréctamente!!'
            error = 'No hay Error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Instruments:poll_list')


# QuestionInterview
class QuestionInterviewList(IsStaffUserMixin, ListView):
    model = QuestionInterview
    template_name = 'Instruments/question_interview_list.html'

    def get_queryset(self):
        interview = Interview.objects.get(id=self.kwargs['pk'])
        queryset = self.model.objects.order_by('name').filter(interview=interview)
        return {'queryset': queryset, 'interview': interview}


class QuestionInterviewCreate(IsStaffUserMixin, CreateView):
    model = QuestionInterview
    form_class = QuestionInterviewForm
    template_name = 'Instruments/question_interview_create.html'

    def get_queryset(self):
        interview = get_object_or_404(
            Interview,
            id=self.kwargs['pk']
        )
        return interview

    def get_context_data(self, **kwargs):
        context = {}
        context["interview"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                interview = self.get_queryset()
                QuestionInterview.objects.create(
                    name=form.cleaned_data.get('name'),
                    text=form.cleaned_data.get('text'),
                    measurementCriterions=form.cleaned_data.get('measurementCriterions'),
                    interview=interview,
                )
                message = 'Pregunta creada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La pregunta no se ha podido crear!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:interview_list')


class QuestionInterviewUpdate(IsStaffUserMixin, UpdateView):
    model = QuestionInterview
    form_class = QuestionInterviewForm
    template_name = 'Instruments/question_interview_update.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = 'Pregunta modificada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La pregunta no se ha podido modificar!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:interview_list')


class QuestionInterviewDelete(IsStaffUserMixin, DeleteView):
    model = QuestionInterview
    template_name = 'Instruments/question_interview_delete.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            question = self.get_object()
            question.delete()
            message = 'Pregunta eliminada corréctamente!!'
            error = 'No hay Error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Instruments:interview_list')


# ObservationCriterions
class ObservationCriterionsList(IsStaffUserMixin, ListView):
    model = ObservationCriterions
    template_name = 'Instruments/observation_criterions_list.html'

    def get_queryset(self):
        observation = Observation.objects.get(id=self.kwargs['pk'])
        queryset = self.model.objects.order_by('criterion').filter(observation=observation)
        return {'queryset': queryset, 'observation': observation}


class ObservationCriterionsCreate(IsStaffUserMixin, CreateView):
    model = ObservationCriterions
    form_class = ObservationCriterionsForm
    template_name = 'Instruments/observation_criterions_create.html'

    def get_queryset(self):
        observation = get_object_or_404(
            Observation,
            id=self.kwargs['pk']
        )
        return observation

    def get_context_data(self, **kwargs):
        context = {}
        context["observation"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                observation = self.get_queryset()
                ObservationCriterions.objects.create(
                    criterion=form.cleaned_data.get('criterion'),
                    measurementCriterions=form.cleaned_data.get('measurementCriterions'),
                    observation=observation,
                )
                message = 'Criterio de observación creada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'El criterio de observación no se ha podido crear!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:observation_list')


class ObservationCriterionsUpdate(IsStaffUserMixin, UpdateView):
    model = ObservationCriterions
    form_class = ObservationCriterionsForm
    template_name = 'Instruments/observation_criterions_update.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():
                form.save()
                message = 'Criterio de observación modificada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'El criterio de observación no se ha podido modificar!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:observation_list')


class ObservationCriterionsDelete(IsStaffUserMixin, DeleteView):
    model = ObservationCriterions
    template_name = 'Instruments/observation_criterions_delete.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            question = self.get_object()
            question.delete()
            message = 'Criterio de observación eliminado corréctamente!!'
            error = 'No hay Error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Instruments:observation_list')
#Review
class ReviewInstruments(IsStaffUserMixin, TemplateView):
    template_name = "Instruments/review_instruments.html"

#ReviewPoll
class ReviewPollList(LoginRequiredMixin, IsStaffUserMixin, ListView):
    model = Poll
    template_name = 'Instruments/review_poll_list.html'

class ReviewAnswersPoll(LoginRequiredMixin, IsStaffUserMixin, ListView):
    model = AnswerPoll 
    template_name = 'Instruments/review_answers_poll_user.html'


    def get_queryset(self):
        poll = get_object_or_404(Poll, id=self.kwargs['pk'])
        user_responses = AnswerPoll.objects.filter(questionPoll__poll=poll).values('user').distinct()
        return user_responses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_responses = self.get_queryset()
        context['poll'] = get_object_or_404(Poll, id=self.kwargs['pk'])
        context['users'] = User.objects.filter(id__in=user_responses)
        return context
    
class ReviewAnswersPollUser(LoginRequiredMixin, IsStaffUserMixin, ListView):
    model = AnswerPoll
    template_name = 'Instruments/review_answers_poll.html'

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        poll_id = self.kwargs['poll_id']
        user_responses = self.model.objects.filter(user_id=user_id, questionPoll__poll_id=poll_id)
        return user_responses
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = get_object_or_404(Poll, id=self.kwargs['poll_id'])
        context['poll'] = poll
        context['user_responses'] = self.get_queryset()
        return context
        

class ReviewPoll(LoginRequiredMixin, IsStaffUserMixin, UpdateView):
    model = AnswerPoll
    form_class = ReviewPollForm
    template_name = 'Instruments/review_poll.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():  
                form.save()
                message = 'Valor otorgado correctamente'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'Valor no otorgado'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:poll_review_list')


class GetResultPoll(LoginRequiredMixin, IsStaffUserMixin, TemplateView):
    template_name = 'Instruments/result.html'

    def get(self, request, *args, **kwargs):
        variable_id = get_variable_poll(answer_id=self.kwargs['answer_id'])
        user_id = self.kwargs['user_id'] 
        variable_result = calculate_variable_poll(variable_id=variable_id, user_id=user_id)
        scale = decide_scale(variable_id=variable_id, variable_value=variable_result)
        return render(request, self.template_name, {'variable_result': variable_result, 'scale': scale})


#ReviewInterview
class ReviewInterviewList(LoginRequiredMixin, IsStaffUserMixin, ListView):
    model = Interview
    template_name = 'Instruments/review_interview_list.html'

class ReviewAnswersInterview(LoginRequiredMixin, IsStaffUserMixin, ListView):
    model = AnswerInterview 
    template_name = 'Instruments/review_answers_interview_user.html'


    def get_queryset(self):
        interview = get_object_or_404(Interview, id=self.kwargs['pk'])
        user_responses = AnswerInterview.objects.filter(questionInterview__interview=interview).values('user').distinct()
        return user_responses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_responses = self.get_queryset()
        context['interview'] = get_object_or_404(Interview, id=self.kwargs['pk'])
        context['users'] = User.objects.filter(id__in=user_responses)
        return context

class ReviewAnswersInterviewUser(LoginRequiredMixin, IsStaffUserMixin, ListView):
    model = AnswerInterview
    template_name = 'Instruments/review_answers_interview.html'

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        interview_id = self.kwargs['interview_id']
        user_responses = self.model.objects.filter(user_id=user_id, questionInterview__interview_id=interview_id)
        return user_responses
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        interview = get_object_or_404(Interview, id=self.kwargs['interview_id'])
        context['interview'] = interview
        context['user_responses'] = self.get_queryset()
        return context

class ReviewInterview(LoginRequiredMixin, IsStaffUserMixin, UpdateView):
    model = AnswerInterview
    form_class = ReviewInterviewForm
    template_name = 'Instruments/review_interview.html'

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance=self.get_object())
            if form.is_valid():  
                form.save()
                message = 'Valor otorgado correctamente'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'Valor no otorgado'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Instruments:interview_review_list')

class GetResultInterview(LoginRequiredMixin, IsStaffUserMixin, TemplateView):
    template_name = 'Instruments/result.html'

    def get(self, request, *args, **kwargs):
        variable_id = get_variable_interview(answer_id=self.kwargs['answer_id'])
        user_id = self.kwargs['user_id'] 
        variable_result = calculate_variable_interview(variable_id=variable_id, user_id=user_id)
        scale = decide_scale(variable_id=variable_id, variable_value=variable_result)
        return render(request, self.template_name, {'variable_result': variable_result, 'scale': scale})

#ReviewObservation
class ReviewObservationList(LoginRequiredMixin, IsStaffUserMixin, ListView):
    model = Observation
    template_name = 'Instruments/review_observation_list.html'

class ReviewObservation(LoginRequiredMixin, IsStaffUserMixin, ListView):
    model = ObservationResult 
    template_name = 'Instruments/review_observation_result_user.html'


    def get_queryset(self):
        observation = get_object_or_404(Observation, id=self.kwargs['pk'])
        user_responses = ObservationResult.objects.filter(observationCriterions__observation=observation).values('user').distinct()
        return user_responses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_responses = self.get_queryset()
        context['observation'] = get_object_or_404(Observation, id=self.kwargs['pk'])
        context['users'] = User.objects.filter(id__in=user_responses)
        return context

class ReviewObservationUser(LoginRequiredMixin, IsStaffUserMixin, ListView):
    model = ObservationResult
    template_name = 'Instruments/review_observation_result.html'

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        observation_id = self.kwargs['observation_id']
        user_responses = self.model.objects.filter(user_id=user_id, observationCriterions__observation_id=observation_id)
        return user_responses
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        observation = get_object_or_404(Observation, id=self.kwargs['observation_id'])
        context['observation'] = observation
        context['user_responses'] = self.get_queryset()
        return context

class GetResultObservation(LoginRequiredMixin, IsStaffUserMixin, TemplateView):
    template_name = 'Instruments/result.html'

    def get(self, request, *args, **kwargs):
        variable_id = get_variable_observation(answer_id=self.kwargs['answer_id'])
        user_id = self.kwargs['user_id'] 
        variable_result = calculate_variable_observation(variable_id=variable_id, user_id=user_id)
        scale = decide_scale(variable_id=variable_id, variable_value=variable_result)
        return render(request, self.template_name, {'variable_result': variable_result, 'scale': scale})