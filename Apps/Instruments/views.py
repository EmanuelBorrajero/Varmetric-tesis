from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import *
from .forms import *

class Instruments(TemplateView):
    template_name = "Instruments/instruments.html"

#Poll
class PollList(ListView):
    model = Poll
    template_name= 'Instruments/poll_list.html'

class PollCreate(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'Instruments/poll_create.html'

    def post(self,request,*args,**kwargs):
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

class PollUpdate(UpdateView):
    model = Poll
    form_class = PollForm
    template_name = 'Instruments/poll_update.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
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

class PollDelete(DeleteView):
    model = Poll
    template_name = 'Instruments/poll_delete.html'

    def post(self,request,*args,**kwargs):
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

class PollDetail(DetailView):
    model = Poll
    template_name = 'Instruments/poll_detail.html'

#Interview
class InterviewList(ListView):
    model = Interview
    template_name= 'Instruments/interview_list.html'

class InterviewCreate(CreateView):
    model = Interview
    form_class = InterviewForm
    template_name = 'Instruments/interview_create.html'

    def post(self,request,*args,**kwargs):
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

class InterviewUpdate(UpdateView):
    model = Interview
    form_class = InterviewForm
    template_name = 'Instruments/interview_update.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
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

class InterviewDelete(DeleteView):
    model = Interview
    template_name = 'Instruments/interview_delete.html'

    def post(self,request,*args,**kwargs):
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

class InterviewDetail(DetailView):
    model = Interview
    template_name = 'Instruments/interview_detail.html'

#Observation
class ObservationList(ListView):
    model = Observation
    template_name= 'Instruments/observation_list.html'

class ObservationCreate(CreateView):
    model = Observation
    form_class = ObservationForm
    template_name = 'Instruments/observation_create.html'

    def post(self,request,*args,**kwargs):
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

class ObservationUpdate(UpdateView):
    model = Observation
    form_class = ObservationForm
    template_name = 'Instruments/observation_update.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
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

class ObservationDelete(DeleteView):
    model = Observation
    template_name = 'Instruments/observation_delete.html'

    def post(self,request,*args,**kwargs):
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

class ObservationDetail(DetailView):
    model = Observation
    template_name = 'Instruments/observation_detail.html'

#QuestionPoll
class QuestionPollList(ListView):
    model = QuestionPoll
    template_name= 'Instruments/question_poll_list.html'

    def get_queryset(self):
        poll = Poll.objects.get(id = self.kwargs['pk'])
        queryset = self.model.objects.filter(poll = poll)
        return {'queryset': queryset, 'poll': poll}

class QuestionPollCreate(CreateView):
    model = QuestionPoll
    form_class = QuestionPollForm
    template_name = 'Instruments/question_poll_create.html'

    def get_queryset(self):
        poll = get_object_or_404(
                    Poll,
                    id = self.kwargs['pk']
                )
        return poll

    def get_context_data(self, **kwargs):
        context = {}
        context["poll"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                poll = self.get_queryset()
                QuestionPoll.objects.create(
                    name = form.cleaned_data.get('name'),
                    text = form.cleaned_data.get('text'),
                    measurementCriterions = form.cleaned_data.get('measurementCriterions'),
                    poll = poll,
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

class QuestionPollUpdate(UpdateView):
    model = QuestionPoll
    form_class = QuestionPollForm
    template_name = 'Instruments/question_poll_update.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
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

class QuestionPollDelete(DeleteView):
    model = QuestionPoll
    template_name = 'Instruments/question_poll_delete.html'

    def post(self,request,*args,**kwargs):
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

#QuestionInterview
class QuestionInterviewList(ListView):
    model = QuestionInterview
    template_name= 'Instruments/question_interview_list.html'

    def get_queryset(self):
        interview = Interview.objects.get(id = self.kwargs['pk'])
        queryset = self.model.objects.filter(interview = interview)
        return {'queryset': queryset, 'interview': interview}

class QuestionInterviewCreate(CreateView):
    model = QuestionInterview
    form_class = QuestionInterviewForm
    template_name = 'Instruments/question_interview_create.html'

    def get_queryset(self):
        interview = get_object_or_404(
                    Interview,
                    id = self.kwargs['pk']
                )
        return interview

    def get_context_data(self, **kwargs):
        context = {}
        context["interview"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                interview = self.get_queryset()
                QuestionInterview.objects.create(
                    name = form.cleaned_data.get('name'),
                    text = form.cleaned_data.get('text'),
                    measurementCriterions = form.cleaned_data.get('measurementCriterions'),
                    interview = interview,
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

class QuestionInterviewUpdate(UpdateView):
    model = QuestionInterview
    form_class = QuestionInterviewForm
    template_name = 'Instruments/question_interview_update.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
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

class QuestionInterviewDelete(DeleteView):
    model = QuestionInterview
    template_name = 'Instruments/question_interview_delete.html'

    def post(self,request,*args,**kwargs):
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

#ObservationCriterions
class ObservationCriterionsList(ListView):
    model = ObservationCriterions
    template_name= 'Instruments/observation_criterions_list.html'

    def get_queryset(self):
        observation = Observation.objects.get(id = self.kwargs['pk'])
        queryset = self.model.objects.filter(observation = observation)
        return {'queryset': queryset, 'observation': observation}

class ObservationCriterionsCreate(CreateView):
    model = ObservationCriterions
    form_class = ObservationCriterionsForm
    template_name = 'Instruments/observation_criterions_create.html'

    def get_queryset(self):
        observation = get_object_or_404(
                    Observation,
                    id = self.kwargs['pk']
                )
        return observation

    def get_context_data(self, **kwargs):
        context = {}
        context["observation"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                observation = self.get_queryset()
                ObservationCriterions.objects.create(
                    measurementCriterions = form.cleaned_data.get('measurementCriterions'),
                    observation = observation,
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

class ObservationCriterionsUpdate(UpdateView):
    model = ObservationCriterions
    form_class = ObservationCriterionsForm
    template_name = 'Instruments/observation_criterions_update.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
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

class ObservationCriterionsDelete(DeleteView):
    model = ObservationCriterions
    template_name = 'Instruments/observation_criterions_delete.html'

    def post(self,request,*args,**kwargs):
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

