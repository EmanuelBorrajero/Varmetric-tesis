from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from .calculation import calculate_intervals
from .models import *
from .forms import *

#Variables
class VariableLIst(ListView):
    model = Variable
    template_name= 'Metrics/varieble_list.html'

class VariableCreate(CreateView):
    model = Variable
    form_class = VariableForm
    template_name = 'Metrics/variable_create.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                message = 'Variable creada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La variable no se ha podido crear!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Metrics:variable_list')

class VariableDetail(DetailView):
    model = Variable
    template_name = 'Metrics/variable_detail.html'

#Dimensions
class DimensionLIst(ListView):
    model = Dimension
    template_name= 'Metrics/variable_dimensions.html'

    def get_queryset(self):
        variable = Variable.objects.get(id = self.kwargs['pk'])
        queryset = self.model.objects.filter(variable = variable)
        return {'queryset': queryset, 'variable': variable}

class DimensionCreate(CreateView):
    model = Dimension
    form_class = DimensionForm
    template_name = 'Metrics/dimension_create.html'

    def get_queryset(self):
        variable = get_object_or_404(
                    Variable,
                    id = self.kwargs['pk']
                )
        return variable

    def get_context_data(self, **kwargs):
        context = {}
        context["variable"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                variable = self.get_queryset()
                Dimension.objects.create(
                    name = form.cleaned_data.get('name'),
                    description = form.cleaned_data.get('description'),
                    weigh = form.cleaned_data.get('weigh'),
                    variable = variable,
                )
                message = 'Dimensión creada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La dimensión no se ha podido crear!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Metrics:dimension_list')

class DimensionDetail(DetailView):
    model = Dimension
    template_name = 'Metrics/dimension_detail.html'

#Indicators
class IndicatorLIst(ListView):
    model = Indicator
    template_name= 'Metrics/dimensions_indicator.html'

    def get_queryset(self):
        dimension = Dimension.objects.get(id = self.kwargs['pk'])
        queryset = self.model.objects.filter(dimension = dimension)
        return {'queryset': queryset, 'dimension': dimension}

class IndicatorCreate(CreateView):
    model = Indicator
    form_class = IndicatorForm
    template_name = 'Metrics/indicator_create.html'

    def get_queryset(self):
        dimension = get_object_or_404(
                    Dimension,
                    id = self.kwargs['pk']
                )
        return dimension

    def get_context_data(self, **kwargs):
        context = {}
        context["dimension"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                dimension = self.get_queryset()
                Indicator.objects.create(
                    name = form.cleaned_data.get('name'),
                    description = form.cleaned_data.get('description'),
                    weigh = form.cleaned_data.get('weigh'),
                    dimension = dimension,
                )
                message = 'Indicador creado corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'El Indicador no se ha podido crear!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Metrics:indicator_list')

class IndicatorDetail(DetailView):
    model = Indicator
    template_name = 'Metrics/indicator_detail.html'

#Measurement Criterion
class MeasurementCriterionLIst(ListView):
    model = MeasurementCriterion
    template_name= 'Metrics/indicator_measurement_criterion.html'

    def get_queryset(self):
        indicator = Indicator.objects.get(id = self.kwargs['pk'])
        queryset = self.model.objects.filter(indicator = indicator)
        return {'queryset': queryset, 'indicator': indicator}

class MeasurementCriterionCreate(CreateView):
    model = MeasurementCriterion
    form_class = MeasurementCriterionForm
    template_name = 'Metrics/measurement_criterion_create.html'

    def get_queryset(self):
        indicator = get_object_or_404(
                    Indicator,
                    id = self.kwargs['pk']
                )
        return indicator

    def get_context_data(self, **kwargs):
        context = {}
        context["indicator"] = self.get_queryset()
        context["form"] = self.form_class
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                indicator = self.get_queryset()
                MeasurementCriterion.objects.create(
                    name = form.cleaned_data.get('name'),
                    description = form.cleaned_data.get('description'),
                    indicator = indicator,
                )
                message = 'Criterio de Medida creado corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'El Criterio de Medida no se ha podido crear!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Metrics:measurement_criterion_list')
