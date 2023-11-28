from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from AprendizajeCreativo.mixins import IsStaffUserMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from .forms import *

#Variables
class VariableLIst(IsStaffUserMixin, ListView):
    model = Variable
    template_name= 'Metrics/varieble_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset

class VariableCreate(IsStaffUserMixin, CreateView):
    model = Variable
    form_class = VariableForm
    template_name = 'Metrics/variable_create.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST)
            if form.is_valid():
                self.model.objects.create(
                    name = form.cleaned_data.get('name'),
                    description = form.cleaned_data.get('description'),
                    user = self.request.user
                )
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

class VariableUpdate(IsStaffUserMixin, UpdateView):
    model = Variable
    form_class = VariableForm
    template_name = 'Metrics/variable_update.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                message = 'Variable modificada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La variable no se ha podido modificar!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Metrics:variable_list')

class VariableDelete(IsStaffUserMixin, DeleteView):
    model = Variable
    template_name = 'Metrics/variable_delete.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            variable = self.get_object()
            variable.delete()
            message = 'Variable eliminada corréctamente!!'
            error = 'No hay Error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Metrics:variable_list')

#Dimensions
class DimensionLIst(IsStaffUserMixin, ListView):
    model = Dimension
    template_name= 'Metrics/variable_dimensions.html'

    def get_queryset(self):
        variable = Variable.objects.get(id = self.kwargs['pk'])
        queryset = self.model.objects.order_by('name').filter(variable = variable)
        return {'queryset': queryset, 'variable': variable}

class DimensionCreate(IsStaffUserMixin, CreateView):
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

class DimensionUpdate(IsStaffUserMixin, UpdateView):
    model = Dimension
    form_class = DimensionForm
    template_name = 'Metrics/dimension_update.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                message = 'Dimensión modificada corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'La dimensión no se ha podido modificar!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Metrics:dimension_list')

class DimensionDelete(IsStaffUserMixin, DeleteView):
    model = Dimension
    template_name = 'Metrics/dimension_delete.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            dimension = self.get_object()
            dimension.delete()
            message = 'Dimensión eliminada corréctamente!!'
            error = 'No hay Error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Metrics:dimension_list')


class DimensionDetail(IsStaffUserMixin, DetailView):
    model = Dimension
    template_name = 'Metrics/dimension_detail.html'

#Indicators
class IndicatorLIst(IsStaffUserMixin, ListView):
    model = Indicator
    template_name= 'Metrics/dimensions_indicator.html'

    def get_queryset(self):
        dimension = Dimension.objects.get(id = self.kwargs['pk'])
        queryset = self.model.objects.order_by('name').filter(dimension = dimension)
        return {'queryset': queryset, 'dimension': dimension}

class IndicatorCreate(IsStaffUserMixin, CreateView):
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

class IndicatorUpdate(IsStaffUserMixin, UpdateView):
    model = Indicator
    form_class = IndicatorForm
    template_name = 'Metrics/indicator_update.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                message = 'Indicador modificado corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'El Indicador no se ha podido modificar!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Metrics:indicator_list')

class IndicatorDelete(IsStaffUserMixin, DeleteView):
    model = Indicator
    template_name = 'Metrics/indicator_delete.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            indicator = self.get_object()
            indicator.delete()
            message = 'Indicador eliminado corréctamente!!'
            error = 'No hay Error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Metrics:indicator_list')

class IndicatorDetail(IsStaffUserMixin, DetailView):
    model = Indicator
    template_name = 'Metrics/indicator_detail.html'

#Measurement Criterion
class MeasurementCriterionLIst(IsStaffUserMixin, ListView):
    model = MeasurementCriterion
    template_name= 'Metrics/indicator_measurement_criterion.html'

    def get_queryset(self):
        indicator = Indicator.objects.get(id = self.kwargs['pk'])
        queryset = self.model.objects.order_by('name').filter(indicator = indicator)
        return {'queryset': queryset, 'indicator': indicator}

class MeasurementCriterionCreate(IsStaffUserMixin, CreateView):
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
                    min_value = form.cleaned_data.get('min_value'),
                    max_value = form.cleaned_data.get('max_value'),
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

class MeasurementCriterionUpdate(IsStaffUserMixin, UpdateView):
    model = MeasurementCriterion
    form_class = MeasurementCriterionForm
    template_name = 'Metrics/measurement_criterion_update.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                message = 'Criterio de Medida modificado corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'El Criterio de Medida no se ha podido modificar!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Metrics:measurement_criterion_list')

class MeasurementCriterionDelete(IsStaffUserMixin, DeleteView):
    model = MeasurementCriterion
    template_name = 'Metrics/measurement_criterion_delete.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            measurement_criterion = self.get_object()
            measurement_criterion.delete()
            message = 'Criterio de Medida eliminado corréctamente!!'
            error = 'No hay Error'
            response = JsonResponse({'message': message, 'error': error})
            response.status_code = 201
            return response
        else:
            return redirect('Metrics:measurement_criterion_list')

class MeasurementCriterionDetail(IsStaffUserMixin, DetailView):
    model = MeasurementCriterion
    template_name = 'Metrics/measurement_criterion_detail.html'

class VariableScaleLIst(ListView):
    model = Variable
    template_name= 'Metrics/varieble_scale_list.html'

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        context = {}
        context["variable"] = self.get_queryset()
        for variable in context["variable"]:
            scale = Scale.objects.filter(scale=variable)
            if scale:
                variable.have_scale = True
            else:
                variable.have_scale = False
        return context

class ScaleLIst(IsStaffUserMixin, ListView):
    model = Scale
    template_name= 'Metrics/scale_list.html'
    success_url = reverse_lazy('Metrics:variable_scale_list')

    def get_queryset(self):
        variable = get_object_or_404(
                    Variable,
                    id = self.kwargs['pk']
                )
        return variable

    def get_context_data(self, **kwargs):
        context = {}
        context["variable"] = self.get_queryset()
        context["scale"] = self.model.objects.filter(scale=self.kwargs['pk']).order_by('initial_value')
        return context
    
    def post(self, request, *args, **kwargs):
        if 'delete_selected' in request.POST:
            variable = get_object_or_404(
                    Variable,
                    id = self.kwargs['pk']
                )
            self.model.objects.filter(scale=variable).delete()
            return redirect(self.success_url)
        else:
            return super().post(request, *args, **kwargs)

class VariableScaleCreate(IsStaffUserMixin, CreateView):
    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            from .functions import createScale
            count = request.POST['count']
            var_id = request.POST['var_id']
            createScale(count, var_id)
            responce = JsonResponse({'url': '/metricas/listado/variables/escala/', 'var_id': var_id})
            responce.status_code = 201
            return responce
        else:
            return redirect('Metrics:variable_scale_list')

    
class VariableScaleUpdate(IsStaffUserMixin, UpdateView):
    model = Scale
    form_class = ScaleForm
    template_name = 'Metrics/scale_create.html'

    def post(self,request,*args,**kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(request.POST, instance = self.get_object())
            if form.is_valid():
                form.save()
                message = 'Etiqueta Lingüística añadida corréctamente!!'
                error = 'No hay Error'
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 201
                return responce
            else:
                message = 'Etiqueta Lingüística no añadida!!'
                error = form.errors
                responce = JsonResponse({'message': message, 'error': error})
                responce.status_code = 400
                return responce
        else:
            return redirect('Metrics:variable_scale_list')

