from django import forms
from django.core.exceptions import ValidationError 
from .models import *

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
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
                    'placeholder': 'Nombre de la Encuesta...',
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
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
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
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en la Descripción')
        return description

class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = [
            'name',
            'description',
            'observationCriterions',
        ]
        labels = {
            'name': 'Nombre*',
            'description': 'Descripción*',
            'observationCriterions': 'Criterios de Observación*',


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
            'observationCriterions': forms.CheckboxSelectMultiple(),
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
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en la Descripción')
        return description

class QuestionPollForm(forms.ModelForm):
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

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for char in description:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en la Descripción')
        return description

class QuestionInterviewForm(forms.ModelForm):
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

    def clean_description(self):
        description = self.cleaned_data.get('description')
        for char in description:
            if char in'`!@#$%^&*()_=+-}{][></"\|~':
                raise ValidationError('Caracteres incorrectos en la Descripción')
        return description