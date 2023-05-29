from django import forms
from django.core.exceptions import ValidationError 
from .models import *

class VariableForm(forms.ModelForm):
    class Meta:
        model = Variable
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
                    'placeholder': 'Nombre de la Variable...',
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

class DimensionForm(forms.ModelForm):
    class Meta:
        model = Dimension
        fields = [
            'name',
            'description',
            'weigh',
        ]
        labels = {
            'name': 'Nombre*',
            'description': 'Descripción*',
            'weigh': 'Peso*',


        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre de la Dimensión...',
                    }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Ingrese una breve descripción',
                    }),
            'weigh': forms.NumberInput(
                attrs={
                    'class': 'form-control',
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

class IndicatorForm(forms.ModelForm):
    class Meta:
        model = Indicator
        fields = [
            'name',
            'description',
            'weigh',
        ]
        labels = {
            'name': 'Nombre*',
            'description': 'Descripción*',
            'weigh': 'Peso*',


        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del Indicador...',
                    }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '2',
                    'placeholder': 'Ingrese una breve descripción',
                    }),
            'weigh': forms.NumberInput(
                attrs={
                    'class': 'form-control',
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

class MeasurementCriterionForm(forms.ModelForm):
    class Meta:
        model = MeasurementCriterion
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
                    'placeholder': 'Nombre del Criterio de Medida...',
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