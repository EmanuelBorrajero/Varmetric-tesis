from django import forms
from django.core.exceptions import ValidationError 
from .models import *

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = [
            'name',
            'description',
            'anonymous',
        ]
        labels = {
            'name': 'Nombre*',
            'description': 'Descripción*',
            'anonymous': 'Anónimo:',


        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la Encuesta...',
                    }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Ingrese una breve descripción',
                    }),
            'anonymous': forms.CheckboxInput(
                attrs={
                    'class': 'ms-2 mt-1',
                }
            )
        }
    def clean_name(self):
        name = self.cleaned_data.get('name')
        for char in name:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en el Nombre')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for char in description:
            if char in'`!@#$%^&*()_=+}{][><\|~':
                raise ValidationError('Caracteres incorrectos en la Descripción')
        return description

class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = [
            'name',
            'description',
        ]
        labels = {
            'name': 'Nombre*',
            'description': 'Descripción*',


        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la Entrevista...',
                    }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Ingrese una breve descripción',
                    }),
        }
    def clean_name(self):
        name = self.cleaned_data.get('name')
        for char in name:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en el Nombre')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for char in description:
            if char in'`!@#$%^&*()_=+}{][><\|~':
                raise ValidationError('Caracteres incorrectos en la Descripción')
        return description

class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = [
            'name',
            'description',
        ]
        labels = {
            'name': 'Nombre*',
            'description': 'Descripción*',


        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la Observación...',
                    }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Ingrese una breve descripción',
                    }),
        }
    def clean_name(self):
        name = self.cleaned_data.get('name')
        for char in name:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en el Nombre')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for char in description:
            if char in'`!@#$%^&*()_=+}{][><\|~':
                raise ValidationError('Caracteres incorrectos en la Descripción')
        return description

class QuestionPollForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionPollForm, self).__init__(*args, **kwargs)
        self.fields['measurementCriterions'].queryset = MeasurementCriterion.objects.order_by('name')

    class Meta:
        model = QuestionPoll
        fields = [
            'name',
            'text',
            'measurementCriterions',
        ]
        labels = {
            'name': 'Nombre*',
            'text': 'Texto de la pregunta*',
            'measurementCriterions': 'Criterio de Medida*',


        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la Pregunta...',
                    }),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Ingrese el texto de la pregunta',
                    }),
            'measurementCriterions': forms.Select(
                attrs={
                    'class': 'form-control form-select',
                    }),
        }
    def clean_name(self):
        name = self.cleaned_data.get('name')
        for char in name:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en el Nombre')
        return name

    def clean_text(self):
        text = self.cleaned_data.get('text')
        for char in text:
            if char in'`!@#$%^&*_=+}{][><\|~':
                raise ValidationError('Caracteres incorrectos en el texto de la pregunta')
        return text

class QuestionInterviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QuestionInterviewForm, self).__init__(*args, **kwargs)
        self.fields['measurementCriterions'].queryset = MeasurementCriterion.objects.order_by('name')
    class Meta:
        model = QuestionInterview
        fields = [
            'name',
            'text',
            'measurementCriterions',
        ]
        labels = {
            'name': 'Nombre*',
            'text': 'Texto de la pregunta*',
            'measurementCriterions': 'Criterio de Medida*',


        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la Pregunta...',
                    }),
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Ingrese el texto de la pregunta',
                    }),
            'measurementCriterions': forms.Select(
                attrs={
                    'class': 'form-control form-select',
                    }),
        }
    def clean_name(self):
        name = self.cleaned_data.get('name')
        for char in name:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en el Nombre')
        return name

    def clean_text(self):
        text = self.cleaned_data.get('text')
        for char in text:
            if char in'`!@#$%^&*_=+}{][><\|~':
                raise ValidationError('Caracteres incorrectos en el texto de la pregunta')
        return text

class ObservationCriterionsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ObservationCriterionsForm, self).__init__(*args, **kwargs)
        self.fields['measurementCriterions'].queryset = MeasurementCriterion.objects.order_by('name')   
    class Meta:
        model = ObservationCriterions
        fields = [
            'criterion',
            'measurementCriterions',
        ]
        labels = {
            'criterion': 'Criterio a Observar',
            'measurementCriterions': 'Criterio*',
        }
        widgets = {
            'criterion': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'measurementCriterions': forms.Select(
                attrs={
                    'class': 'form-control form-select',
                    }),
        }


class ReviewPollForm(forms.ModelForm):
    value = forms.FloatField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs:
            measurement_criterion = kwargs['instance'].questionPoll.measurementCriterions
            self.fields['value'].label = measurement_criterion.description
            self.fields['value'].widget.attrs['min'] = measurement_criterion.min_value
            self.fields['value'].widget.attrs['max'] = measurement_criterion.max_value
            self.fields['value'].widget.attrs['class'] = 'form-control mt-2'

    class Meta:
        model = AnswerPoll
        fields = ('value', )

    def clean(self):
        cleaned_data = super().clean()
        value = cleaned_data.get('value')
        measurement_criterion = self.instance.questionPoll.measurementCriterions
        if value < measurement_criterion.min_value or value > measurement_criterion.max_value:
            raise forms.ValidationError("El valor debe estar dentro del rango permitido. "+str(measurement_criterion.min_value)+" - "+str(measurement_criterion.max_value))
        return cleaned_data
    
class ReviewInterviewForm(forms.ModelForm):
    value = forms.FloatField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs:
            measurement_criterion = kwargs['instance'].questionInterview.measurementCriterions
            self.fields['value'].label = measurement_criterion.description
            self.fields['value'].widget.attrs['min'] = measurement_criterion.min_value
            self.fields['value'].widget.attrs['max'] = measurement_criterion.max_value
            self.fields['value'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = AnswerInterview
        fields = ('value', )
    
    def clean(self):
        cleaned_data = super().clean()
        value = cleaned_data.get('value')
        measurement_criterion = self.instance.questionInterview.measurementCriterions
        if value < measurement_criterion.min_value or value > measurement_criterion.max_value:
            raise forms.ValidationError("El valor debe estar dentro del rango permitido. "+str(measurement_criterion.min_value)+" - "+str(measurement_criterion.max_value))
        return cleaned_data

